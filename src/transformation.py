import pandas as pd

def prepare_date_features(df):

    df["order_date"] = pd.to_datetime(
        df["order_date"]
    )

    df["month"] = df["order_date"].dt.month

    df["month_name"] = (
        df["order_date"].dt.month_name()
    )

    df["year"] = df["order_date"].dt.year

    return df