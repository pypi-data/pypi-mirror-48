import json

import pg

from awswrangler.exceptions import (
    RedshiftLoadError,
    UnsupportedType,
    InvalidDataframeType,
)


class Redshift:
    def __init__(self, session):
        self._session = session

    @staticmethod
    def generate_connection(dbname, host, port, user, passwd):
        return pg.DB(dbname=dbname, host=host, port=int(port), user=user, passwd=passwd)

    def get_connection(self, glue_connection):
        conn_details = self._session.glue.get_connection_details(name=glue_connection)
        props = conn_details["ConnectionProperties"]
        host = props["JDBC_CONNECTION_URL"].split(":")[2].replace("/", "")
        port, dbname = props["JDBC_CONNECTION_URL"].split(":")[3].split("/")
        user = props["USERNAME"]
        password = props["PASSWORD"]
        conn = pg.DB(
            dbname=dbname, host=host, port=int(port), user=user, passwd=password
        )
        conn.query("set statement_timeout = 1200000")
        return conn

    def write_load_manifest(self, manifest_path, objects_paths):
        objects_sizes = self._session.s3.get_objects_sizes(objects_paths=objects_paths)
        manifest = {"entries": []}
        for path, size in objects_sizes.items():
            entry = {"url": path, "mandatory": True, "meta": {"content_length": size}}
            manifest.get("entries").append(entry)
        payload = json.dumps(manifest)
        client_s3 = self._session.boto3_session.client("s3")
        bucket, path = manifest_path.replace("s3://", "").split("/", 1)
        client_s3.put_object(Body=payload, Bucket=bucket, Key=path)
        return manifest

    @staticmethod
    def get_number_of_slices(redshift_conn):
        res = redshift_conn.query(
            "SELECT COUNT(*) as count_slices FROM (SELECT DISTINCT node, slice from STV_SLICES)"
        )
        count_slices = res.dictresult()[0]["count_slices"]
        return count_slices

    @staticmethod
    def load_table(
        dataframe,
        dataframe_type,
        manifest_path,
        schema_name,
        table_name,
        redshift_conn,
        num_files,
        iam_role,
        mode="append",
        preserve_index=False,
    ):
        redshift_conn.begin()
        if mode == "overwrite":
            redshift_conn.query(
                "-- AWS DATA WRANGLER\n"
                f"DROP TABLE IF EXISTS {schema_name}.{table_name}"
            )
        schema = Redshift._get_redshift_schema(
            dataframe=dataframe,
            dataframe_type=dataframe_type,
            preserve_index=preserve_index,
        )
        cols_str = "".join([f"{col[0]} {col[1]},\n" for col in schema])[:-2]
        sql = (
            "-- AWS DATA WRANGLER\n"
            f"CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (\n{cols_str}"
            ") DISTSTYLE AUTO"
        )
        redshift_conn.query(sql)
        sql = (
            "-- AWS DATA WRANGLER\n"
            f"COPY {schema_name}.{table_name} FROM '{manifest_path}'\n"
            f"IAM_ROLE '{iam_role}'\n"
            "MANIFEST\n"
            "FORMAT AS PARQUET"
        )
        redshift_conn.query(sql)
        res = redshift_conn.query(
            "-- AWS DATA WRANGLER\n SELECT pg_last_copy_id() AS query_id"
        )
        query_id = res.dictresult()[0]["query_id"]
        sql = (
            "-- AWS DATA WRANGLER\n"
            f"SELECT COUNT(*) as num_files_loaded FROM STL_LOAD_COMMITS WHERE query = {query_id}"
        )
        res = redshift_conn.query(sql)
        num_files_loaded = res.dictresult()[0]["num_files_loaded"]
        if num_files_loaded != num_files:
            redshift_conn.rollback()
            raise RedshiftLoadError(
                f"Redshift load rollbacked. {num_files_loaded} files counted. {num_files} expected."
            )
        redshift_conn.commit()

    @staticmethod
    def _get_redshift_schema(dataframe, dataframe_type, preserve_index=False):
        schema_built = []
        if dataframe_type == "pandas":
            if preserve_index:
                name = str(dataframe.index.name) if dataframe.index.name else "index"
                dataframe.index.name = "index"
                dtype = str(dataframe.index.dtype)
                redshift_type = Redshift._type_pandas2redshift(dtype)
                schema_built.append((name, redshift_type))
            for col in dataframe.columns:
                name = str(col)
                dtype = str(dataframe[name].dtype)
                redshift_type = Redshift._type_pandas2redshift(dtype)
                schema_built.append((name, redshift_type))
        elif dataframe_type == "spark":
            for name, dtype in dataframe.dtypes:
                redshift_type = Redshift._type_spark2redshift(dtype)
                schema_built.append((name, redshift_type))
        else:
            raise InvalidDataframeType(dataframe_type)
        return schema_built

    @staticmethod
    def _type_pandas2redshift(dtype):
        dtype = dtype.lower()
        if dtype == "int32":
            return "INTEGER"
        elif dtype == "int64":
            return "BIGINT"
        elif dtype == "float32":
            return "FLOAT4"
        elif dtype == "float64":
            return "FLOAT8"
        elif dtype == "bool":
            return "BOOLEAN"
        elif dtype == "object" and isinstance(dtype, str):
            return "VARCHAR(256)"
        elif dtype[:10] == "datetime64":
            return "TIMESTAMP"
        else:
            raise UnsupportedType("Unsupported Pandas type: " + dtype)

    @staticmethod
    def _type_spark2redshift(dtype):
        dtype = dtype.lower()
        if dtype == "int":
            return "INTEGER"
        elif dtype == "long":
            return "BIGINT"
        elif dtype == "float":
            return "FLOAT8"
        elif dtype == "bool":
            return "BOOLEAN"
        elif dtype == "string":
            return "VARCHAR(256)"
        elif dtype[:10] == "datetime.datetime":
            return "TIMESTAMP"
        else:
            raise UnsupportedType("Unsupported Spark type: " + dtype)
