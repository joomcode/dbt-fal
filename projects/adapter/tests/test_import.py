from fal.dbt import FalDbt
from pathlib import Path
import os
import pandas as pd

profiles_dir = os.path.join(Path.cwd(), "tests/mock/mockProfile")
project_dir = os.path.join(Path.cwd(), "tests/mock")


def test_initialize():
    faldbt = FalDbt(
        profiles_dir=profiles_dir,
        project_dir=project_dir,
    )

    faldbt.execute_sql("create schema if not exists dbt_fal")

    df = pd.DataFrame({'a': [1]})

    faldbt.write_to_model(df, "model_with_scripts", mode="overwrite")
    faldbt.write_to_source(df, "test_sources", "single_col", mode='overwrite')

    df = faldbt.source("test_sources", "single_col")
    assert df.shape[0] == 1
    df = faldbt.ref("model_with_scripts")
    assert df.shape[0] == 1

    faldbt.write_to_model(df, "model_with_scripts", mode="append")
    faldbt.write_to_source(df, "test_sources", "single_col", mode='append')
    df = faldbt.source("test_sources", "single_col")
    assert df.shape[0] == 2
    df = faldbt.ref("model_with_scripts")
    assert df.shape[0] == 2

    sources = faldbt.list_sources()
    assert "test_sources" in [source.name for source in sources]

    models = faldbt.list_models()
    assert "model_with_scripts" in [model.name for model in models]
