def organize_metrics(metrics):
    report = ""
    
    # 1. Overview
    overview = metrics.get("overview", {})
    report += "## Overview:\n"
    report += f"- Rows: {overview.get('rows', 0)}\n"
    report += f"- Columns: {overview.get('columns', 0)}\n\n"
    
    # 2. Data Quality
    quality = metrics.get("data_quality", {})
    report += "## Data Quality:\n"
    report += f"- Total Missing Values: {quality.get('missing_total', 0)}\n"
    
    missing_by_column = quality.get("missing_by_column", {})
    for col, val in missing_by_column.items():
        report += f"  - {col}: {val} missing\n"
    
    report += "\n"
    
    # 3. Categorical Analysis
    cat = metrics.get("categorical_analysis", {})
    report += "## Categorical Analysis:\n"
    
    for col, counts in cat.items():
        report += f"- {col}:\n"
        for k, v in counts.items():
            report += f"  - {k}: {v}\n"
        report += "\n"
    
    return report
