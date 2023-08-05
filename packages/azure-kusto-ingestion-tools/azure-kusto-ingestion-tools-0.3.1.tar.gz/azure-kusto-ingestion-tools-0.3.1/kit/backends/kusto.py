import logging
from typing import List
from urllib.parse import urlparse

from azure.kusto.data.exceptions import KustoServiceError
from azure.kusto.data.request import KustoClient, KustoConnectionStringBuilder
from azure.kusto.ingest import IngestionProperties, KustoIngestClient, CsvColumnMapping, JsonColumnMapping, ReportMethod, ReportLevel, DataFormat
from azure.kusto.ingest._ingestion_properties import ColumnMapping

from kit.dtypes import dotnet_to_kusto_type
from kit.enums import SchemaConflictMode
from kit.exceptions import DatabaseDoesNotExist, DatabaseConflictError, SchemaConflictError
from kit.models.database import Database, Table, Column
from kit.models.ingestion import IngestionSource
from kit.models.mappings import IngestionMapping

logger = logging.getLogger("kit")

LIST_COLUMNS_BY_TABLE = ".show database {database_name} schema | where TableName != '' and ColumnName != '' | summarize Columns=make_set(strcat(ColumnName,':',ColumnType)) by TableName"
CREATE_INGESTION_MAPPING = """.create table {table} ingestion {mapping_type} mapping "{mapping_name}" '[{mappings}]'"""


class KustoClientProvider:
    def __init__(self, cluster, auth):
        self.target_engine = KustoClientProvider.resolve_engine_uri(cluster)
        self.target_dm = KustoClientProvider.resolve_ingest_uri(self.target_engine)
        self.auth = auth

    @staticmethod
    def resolve_engine_uri(cluster: str):
        uri = urlparse(cluster)

        scheme = uri.scheme if uri.scheme else "https"
        # short style : 'cluster.region'
        if not uri.netloc and uri.path:
            return f"{scheme}://{uri.path}.kusto.windows.net"

        return uri.geturl()

    @staticmethod
    def resolve_ingest_uri(engine_uri: str):

        return "{0.scheme}://ingest-{0.netloc}".format(urlparse(engine_uri))

    def resolve_kcsb(self, uri):
        if "user_token" in self.auth:
            kcsb_f = KustoConnectionStringBuilder.with_aad_user_token_authentication
        if "aad_app_id" in self.auth:
            kcsb_f = KustoConnectionStringBuilder.with_aad_application_key_authentication
        if "user_id" in self.auth:
            kcsb_f = KustoConnectionStringBuilder.with_aad_user_password_authentication

        return kcsb_f(uri, **self.auth)

    def get_engine_client(self):
        return KustoClient(self.resolve_kcsb(self.target_engine))

    def get_dm_client(self):
        return KustoClient(self.resolve_kcsb(self.target_dm))

    def get_ingest_client(self):
        return KustoIngestClient(self.resolve_kcsb(self.target_dm))


class KustoBackend:
    def __init__(self, cluster: str, auth: dict, **kwargs):
        self.client_provider = KustoClientProvider(cluster, auth)

    def describe_database(self, database_name: str, **kwargs) -> Database:
        tables = []
        client = self.client_provider.get_engine_client()
        try:
            tables_result = client.execute("NetDefault", LIST_COLUMNS_BY_TABLE.format(database_name=database_name)).primary_results[0]

            for t in tables_result:
                columns = []
                for index, col in enumerate(t["Columns"]):
                    name, dotnet_type = col.split(":")
                    columns.append(Column(name, index=index, data_type=dotnet_to_kusto_type(dotnet_type)))

                tables.append(Table(t["TableName"], columns))
        except KustoServiceError as e:
            resp = e.http_response.json()
            if "error" in resp and resp["error"]["@type"] == "Kusto.Data.Exceptions.EntityNotFoundException":
                raise DatabaseDoesNotExist(database_name)
            else:
                raise e

        return Database(database_name, tables)

    def enforce_schema(self, database_schema: Database, schema_conflict: SchemaConflictMode = SchemaConflictMode.Append):
        try:
            actual_database = self.describe_database(database_schema.name)

            for expected_table in database_schema.tables:
                if expected_table.name not in actual_database.tables_dict:
                    self.create_table(expected_table, actual_database.name)
                else:
                    if actual_database.tables_dict[expected_table.name] == expected_table:
                        logger.debug(f"Table '{expected_table.name}' exists on database '{actual_database.name}'. Nothing to do.")
                    elif schema_conflict == SchemaConflictMode.Safe:
                        raise SchemaConflictError(
                            f"SAFE MODE: Database '{database_schema.name}' already has a table named '{expected_table.name}' but with a different schema."
                        )
                    else:
                        raise NotImplementedError("should extend table according to schema conflict mode")

        except DatabaseDoesNotExist:
            if schema_conflict == SchemaConflictMode.Safe:
                raise DatabaseConflictError(
                    f'SAFE MODE: Expected a Database named "{database_schema.name}" on {self.client_provider.target_engine} but none found'
                )
            if schema_conflict == SchemaConflictMode.Append:
                # by default, if we can't find a database on the cluster, we will create it
                pass

    @classmethod
    def get_create_ingestion_command(cls, table: str, mapping_name: str, column_mappings: List[ColumnMapping]) -> str:
        mapping_column_class = column_mappings[0].__class__.__name__

        mapping_type = "json" if mapping_column_class.lower().startswith("json") else "csv"

        mappings = []

        for col in column_mappings:
            col_map_str = "{" + ",".join([f'"{prop}":"{name}"' for prop, name in vars(col).items()]) + "}"
            mappings.append(col_map_str)

        mappings_str = ",".join(mappings)
        return CREATE_INGESTION_MAPPING.format(table=table, mapping_type=mapping_type, mapping_name=mapping_name, mappings=mappings_str)

    @classmethod
    def get_create_table_command(cls, table: Table) -> str:
        command_format = ".create table {} ({})"
        column_definitions = []
        for col in table.columns:
            column_definitions.append(f"['{col.name}']:{col.dtype}")

        return command_format.format(table.name, ",".join(column_definitions))

    def create_table(self, table: Table, database_name: str):
        client = self.client_provider.get_engine_client()

        client.execute(database_name, self.get_create_table_command(table))

    def ping(self):
        self.client_provider.get_engine_client().execute("NetDefault", ".show diagnostics")
        self.client_provider.get_dm_client().execute("NetDefault", ".show diagnostics")

    @classmethod
    def get_ingestion_mapping(cls, data_format: str, mapping: IngestionMapping) -> List[ColumnMapping]:
        kusto_ingest_mapping = []

        if data_format == "csv":
            # TODO: need to add __str__ to columnMapping
            mapping_func = lambda source_col, target_col: CsvColumnMapping(target_col.name, target_col.data_type.value, source_col.index)
        if data_format in ["json", "singlejson", "multijson"]:
            # TODO: need to add __str__ to columnMapping
            mapping_func = lambda source_col, target_col: JsonColumnMapping(target_col.name, f"$.{source_col.name}", cslDataType=target_col.data_type.value)

        for col in mapping.columns:
            kusto_ingest_mapping.append(mapping_func(col.source, col.target))

        return kusto_ingest_mapping

    def ingest_from_source(self, source: IngestionSource, mapping: IngestionMapping, target_database: str, target_table: str, **kwargs):
        files = source.files
        ingest_client = self.client_provider.get_ingest_client()

        # TODO: should maybe persist ingestion mappings
        ingestion_props = IngestionProperties(
            target_database,
            target_table,
            dataFormat=DataFormat(source.data_format),
            mapping=self.get_ingestion_mapping(source.data_format, mapping),
            reportLevel=ReportLevel.FailuresOnly,
            reportMethod=ReportMethod.Queue,
            flushImmediately=True,
        )

        if "batch_id" in kwargs and not kwargs.get("no_wait", False):
            # this helps with monitoring
            ingestion_props.ingest_by_tags = [kwargs["batch_id"]]
        for file_path in files:
            if kwargs.get("direct", True):
                # TODO: allow for direct ingestion (this is currently only relevant to files already in storage)
                # client.execute(f'.ingest into table {operation.target} ({}) with ({mapping_ref_key}="{mapping_name}")')
                pass
            else:
                logger.info(f'Queueing "{file_path}" to ingest into "{ingestion_props.table}"')
                ingest_client.ingest_from_file(str(file_path), ingestion_props)

    def count_rows(self, database: str, table: str) -> int:
        client = self.client_provider.get_engine_client()

        result = client.execute(database, f"['{table}'] | count")

        return result.primary_results[0][0][0]

    def peek_table(self, database: str, table: str, n=10) -> List[str]:
        client = self.client_provider.get_engine_client()

        result = client.execute(database, f"['{table}'] | limit {n}")

        return result.primary_results[0]

    def count_rows_with_tag(self, database: str, table: str, tag: str) -> int:
        client = self.client_provider.get_engine_client()

        result = client.execute(database, f"['{table}'] | where extent_tags() has 'ingest-by:{tag}' | count")

        return result.primary_results[0][0][0]

    def get_ingestion_errors(self, database: str, tag: str):
        client = self.client_provider.get_engine_client()

        result = client.execute(
            "NetDefault", f".show ingestion failures | where FailedOn > ago(1h) and Database == '{database}' and IngestionProperties contains ('{tag}')"
        )

        return result.primary_results[0]
