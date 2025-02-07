

def model(dbt, session):
    dbt.config(materialized="table")
    df = dbt.ref("model_a")
    return df.withColumns({'col2': df['col'] + 1})