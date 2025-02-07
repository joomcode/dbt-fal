

def model(dbt, session):
    dbt.config(materialized="table")
    df = dbt.ref("model_a")
    print(3333333333333333333333333)
    return df.withColumns({'col2': df['col'] + 1})