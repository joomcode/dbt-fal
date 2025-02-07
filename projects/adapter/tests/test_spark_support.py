import pytest
from pyspark.sql import SparkSession
import tempfile
import shutil


@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder.master("local[1]").appName("test").getOrCreate()
    yield spark
    spark.stop()


@pytest.fixture
def temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


def test_write_dataframe(spark, temp_dir):
    # Create a simple DataFrame
    data = [("Alice", 29), ("Bob", 31)]
    columns = ["name", "age"]
    df = spark.createDataFrame(data, columns)

    path = f"{temp_dir}/test_table"
    df.write.mode("overwrite").saveAsTable("test_table", path=path)
    df_read = spark.table("test_table")
    assert df.count() == df_read.count()
    assert df.columns == df_read.columns

    # Verify specific data (optional)
    assert df.filter(df.name == "Alice").collect()[0]["age"] == 29
    assert False
