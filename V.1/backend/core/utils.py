import pandas as pd
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]

def save_processed(df: pd.DataFrame, original_raw_path: str) -> str:
    processed_dir = BASE / "data/processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    name = Path(original_raw_path).stem + "_processed.csv"
    dest = processed_dir / name
    df.to_csv(dest, index=False)
    summary = {
        "processed_path": str(dest),
        "rows": int(df.shape[0]),
        "columns": list(df.columns),
    }
    (processed_dir / "last_summary.json").write_text(json.dumps(summary))
    return str(dest)
