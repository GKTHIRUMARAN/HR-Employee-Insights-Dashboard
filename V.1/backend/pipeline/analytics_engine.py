import pandas as pd
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def _load_processed(processed_path: str = None) -> pd.DataFrame:
    if processed_path:
        return pd.read_csv(processed_path)
    summary_file = BASE / "data/processed" / "last_summary.json"
    if not summary_file.exists():
        return pd.DataFrame()
    summary = json.loads(summary_file.read_text())
    return pd.read_csv(summary["processed_path"])

def load_last_processed_summary():
    p = BASE / "data/processed" / "last_summary.json"
    if not p.exists():
        return {"error": "no processed data available"}
    return json.loads(p.read_text())

def build_kpis(processed_path: str = None):
    df = _load_processed(processed_path)
    if df.empty:
        return {"error": "no processed data available"}
    result = {"total_rows": int(df.shape[0])}
    id_cols = [c for c in df.columns if "id" in c.lower()]
    if id_cols:
        result["unique_employees"] = int(df[id_cols[0]].nunique())
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    result["numeric_mean"] = {c: float(df[c].mean()) for c in numeric_cols}
    attr_cols = [c for c in df.columns if "attrit" in c.lower()]
    if attr_cols:
        col = attr_cols[0]
        vals = df[col].astype(str).str.lower()
        positives = vals.isin(["yes","y","true","1"]).sum()
        result["attrition_count"] = int(positives)
        result["attrition_rate"] = float(positives / len(df))
    dept_cols = [c for c in df.columns if "dept" in c.lower()]
    if dept_cols:
        col = dept_cols[0]
        result["department_distribution"] = df[col].value_counts().to_dict()
    return result

def build_charts(processed_path: str = None):
    df = _load_processed(processed_path)
    if df.empty:
        return {"error": "no processed data available"}
    charts = {}
    s_cols = [c for c in df.columns if "salary" in c.lower()]
    if s_cols:
        col = s_cols[0]
        try:
            buckets = pd.cut(df[col], bins=10).value_counts().sort_index()
            charts["salary_buckets"] = [{"label": str(idx), "value": int(v)} for idx, v in buckets.items()]
        except:
            charts["salary_values"] = df[col].describe().to_dict()
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    for c in cat_cols[:4]:
        vc = df[c].value_counts().head(10)
        charts[f"cat_{c}"] = [{"label": str(k), "value": int(v)} for k,v in vc.items()]
    return charts
