from fastapi import APIRouter, UploadFile, File, HTTPException
from core.file_handler import save_upload_file
from pipeline.etl_process import run_etl

router = APIRouter()

@router.post("/run")
async def etl_run(file: UploadFile = File(...)):
    filename = file.filename
    if not (filename.lower().endswith(".csv") or filename.lower().endswith((".xls", ".xlsx"))):
        raise HTTPException(status_code=400, detail="Only CSV and Excel files are supported.")
    raw_path = save_upload_file(file, dest_dir="data/raw")
    result = run_etl(raw_path)
    return result
