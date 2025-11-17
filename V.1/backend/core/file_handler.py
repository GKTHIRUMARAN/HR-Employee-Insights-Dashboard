import os
from pathlib import Path
from fastapi import UploadFile
import shutil
import datetime

BASE = Path(__file__).resolve().parents[1]

def ensure_dirs():
    for d in ["data/raw", "data/processed", "logs"]:
        p = BASE / d
        p.mkdir(parents=True, exist_ok=True)

def save_upload_file(upload_file: UploadFile, dest_dir: str = "data/raw") -> str:
    ensure_dirs()
    dest_folder = BASE / dest_dir
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}__{upload_file.filename}"
    dest_path = dest_folder / filename
    with dest_path.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return str(dest_path)
