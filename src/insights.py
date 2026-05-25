def generate_executive_summary(
    kpis,
    top_region,
    top_customer,
    top_product
):

    summary = f"""

EXECUTIVE SUMMARY
=============================

Total Revenue:
₹{kpis['total_revenue']:,.2f}

Top Region:
{top_region}

Top Customer:
{top_customer}

Best Product:
{top_product}

Average Order Value:
₹{kpis['average_order_value']:,.2f}

"""

    return summary