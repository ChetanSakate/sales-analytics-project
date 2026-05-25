# ==========================================
# CONFIGURATION SETTINGS
# ==========================================

RAW_DATA_PATH = "data/raw/sales_data.csv"

PROCESSED_DATA_PATH = "data/processed/cleaned_sales_data.csv"

HIGH_VALUE_THRESHOLD = 30000

CURRENCY_SYMBOL = "₹"

TOP_CUSTOMERS_LIMIT = 10

FILE_ENCODING = "utf-8"

from src.config import FILE_ENCODING

encoding=FILE_ENCODING