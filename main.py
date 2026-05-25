# ==========================================
# IMPORT MODULES
# ==========================================

from src.ingestion import load_dataset

from src.validation import validate_dataset

from src.transformation import prepare_date_features

from src.analytics import (
    calculate_kpis,
    aggregate_metrics
)

from src.insights import (
    generate_executive_summary
)

from src.export import (
    export_csv,
    export_text
)

from src.config import *

# ==========================================
# LOAD DATA
# ==========================================

df = load_dataset(RAW_DATA_PATH)

# ==========================================
# VALIDATE DATA
# ==========================================

validation_report = validate_dataset(df)

print(validation_report)

# ==========================================
# TRANSFORM DATA
# ==========================================

df = prepare_date_features(df)

# ==========================================
# KPI ENGINE
# ==========================================

kpis = calculate_kpis(df)

# ==========================================
# ANALYTICS
# ==========================================

region_revenue = aggregate_metrics(
    df,
    "region"
)

customer_revenue = aggregate_metrics(
    df,
    "customer_name"
)

product_revenue = aggregate_metrics(
    df,
    "product"
)

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

summary = generate_executive_summary(
    kpis=kpis,
    top_region=region_revenue.iloc[0]["region"],
    top_customer=customer_revenue.iloc[0]["customer_name"],
    top_product=product_revenue.iloc[0]["product"]
)

print(summary)

# ==========================================
# EXPORT REPORTS
# ==========================================

export_csv(
    df,
    PROCESSED_DATA_PATH
)

export_text(
    summary,
    "reports/executive_summary.txt"
)

print("Pipeline completed successfully.")