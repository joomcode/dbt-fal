

def model(dbt, session):
    dbt.config(materialized="incremental")
    df = dbt.ref("model_a")
    return df.withColumns({'col2': df['col'] + 1})