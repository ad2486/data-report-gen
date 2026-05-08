import pandas as pd

def generate_metrics(df):
    metrics = {
        "overview": {
            "rows": df.shape[0],
            "columns": df.shape[1],
        },

        "data_quality": {
            "missing_by_column": df.isnull().sum().to_dict(),
            "missing_total": int(df.isnull().sum().sum())
        },

        "categorical_analysis": {
            col: df[col].value_counts().head(5).to_dict()
            for col in df.select_dtypes(include="object").columns
        }
    }

    return metrics