def validate_dataset(df):

    validation_report = {}

    validation_report["null_values"] = (
        df.isnull().sum().sum()
    )

    validation_report["duplicate_records"] = (
        df.duplicated().sum()
    )

    validation_report["total_rows"] = len(df)

    return validation_report