from attr import dataclass
from dbt.adapters.base import BaseAdapter, BaseRelation
from dbt.adapters.spark import SparkAdapter
from dbt.adapters.spark.connections import SparkConnectionMethod
from pyspark.sql import DataFrame
from dbt.adapters.fal_experimental.adapter_support import new_connection


def read_relation_as_df(adapter: BaseAdapter, relation: BaseRelation) -> DataFrame:
    # raise "ASDLKHASBDKJHASBDJASHBDk"
    sql = f"SELECT * FROM {relation}"

    assert adapter.type() == "spark"

    with new_connection(adapter, "fal-spark:read_relation_as_df") as conn:
        assert conn.credentials.method == SparkConnectionMethod.SESSION
        conn.handle.execute(sql)
        df = conn.handle._df

    return df


def write_df_to_relation(
    adapter: SparkAdapter,
    df: DataFrame,
    relation: BaseRelation,
):
    assert adapter.type() == "spark"

    with new_connection(adapter, "fal-spark:write_df_to_relation") as conn:
        # from pprint import pprint
        # pprint(conn)
        # pprint(conn.credentials)
        assert conn.credentials.method == SparkConnectionMethod.SESSION
        db = relation.database
        table = relation.identifier
        print(f'writing db={db}, table={table}')

        (
            df
            .write
            .mode("overwrite")
            .format("parquet")
            .option("overwriteSchema", "true")
            .saveAsTable(f'{db}.{table}')
        )
