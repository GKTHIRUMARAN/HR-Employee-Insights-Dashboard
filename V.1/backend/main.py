from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import etl, analytics

app = FastAPI(title="HR Data v1 - FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(etl.router, prefix="/etl")
app.include_router(analytics.router, prefix="/analytics")

@app.get("/")
async def root():
    return {"status": "ok", "message": "HR Data v1 API"}
