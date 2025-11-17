import pandas as pd
import numpy as np
from core.utils import save_processed
from pathlib import Path

COMMON_NUMERIC = ["salary", "age", "years_at_company", "tenure"]
COMMON_CATEGORICAL = ["department", "gender", "jobrole", "attrition", "employee_id"]

def _read_any(path: str) -> pd.DataFrame:
    p = Path(path)
    if p.suffix.lower() == ".csv":
        return pd.read_csv(path)
    else:
        return pd.read_excel(path)

def _basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns=lambda c: str(c).strip())
    df = df.drop_duplicates()
    obj_cols = df.select_dtypes(include="object").columns
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip()
    for c in df.columns:
        if pd.api.types.is_numeric_dtype(df[c]):
            df[c] = df[c].fillna(df[c].median())
        else:
            df[c] = df[c].fillna("Unknown")
    return df

def _derive_features(df: pd.DataFrame) -> pd.DataFrame:
    lower_cols = [c.lower() for c in df.columns]
    for s in COMMON_NUMERIC:
        if s in lower_cols:
            col = df.columns[lower_cols.index(s)]
            if "salary" in s:
                try:
                    df["salary_k"] = df[col].apply(lambda x: float(x)/1000 if pd.notna(x) else x)
                except:
                    pass
    return df

def _make_summary(df: pd.DataFrame, processed_path: str):
    stats = {}
    stats["row_count"] = int(df.shape[0])
    stats["col_count"] = int(df.shape[1])
    numeric = df.select_dtypes(include="number").columns.tolist()
    stats["numeric_columns"] = numeric
    stats["numeric_stats"] = {}
    for c in numeric:
        stats["numeric_stats"][c] = {
            "mean": float(df[c].mean()),
            "median": float(df[c].median()),
            "min": float(df[c].min()),
            "max": float(df[c].max()),
        }
    cat = df.select_dtypes(include="object").columns.tolist()
    stats["categorical_top"] = {}
    for c in cat:
        top = df[c].value_counts().head(5).to_dict()
        stats["categorical_top"][c] = top
    stats["processed_path"] = processed_path
    return stats

def run_etl(raw_path: str) -> dict:
    df = _read_any(raw_path)
    df = _basic_clean(df)
    df = _derive_features(df)
    processed_path = save_processed(df, raw_path)
    summary = _make_summary(df, processed_path)
    return {"etl_summary": summary, "processed_path": processed_path}
