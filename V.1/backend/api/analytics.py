from fastapi import APIRouter, Query
from pipeline.analytics_engine import load_last_processed_summary, build_kpis, build_charts

router = APIRouter()

@router.get("/kpis")
def get_kpis(processed_path: str = Query(None)):
    if processed_path:
        return build_kpis(processed_path)
    return load_last_processed_summary()

@router.get("/charts")
def get_charts(processed_path: str = Query(None)):
    if processed_path:
        return build_charts(processed_path)
    return build_charts()
