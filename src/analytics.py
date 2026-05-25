# ==========================================
# ANALYTICS FUNCTIONS
# ==========================================

def calculate_kpis(df):

    """
    Calculate executive KPIs.
    """

    kpis = {

        "total_revenue":
        df["revenue"].sum(),

        "total_orders":
        df["order_id"].nunique(),

        "average_order_value":
        df["revenue"].mean(),

        "total_customers":
        df["customer_name"].nunique(),

        "total_quantity_sold":
        df["quantity"].sum()
    }

    return kpis


# ==========================================
# GENERIC AGGREGATION FUNCTION
# ==========================================

def aggregate_metrics(
    df,
    group_column,
    metric_column="revenue",
    agg_function="sum"
):

    """
    Reusable aggregation engine.
    """

    result = (
        df.groupby(group_column)[metric_column]
          .agg(agg_function)
          .sort_values(ascending=False)
          .reset_index()
    )

    return result