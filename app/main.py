from fastapi import FastAPI
from fastapi import FastAPI
from app.api.v1.quote import router as quote_router

app = FastAPI(title="OnsiteWash Backend")

app.include_router(quote_router, prefix="/api/v1")

@app.get("/")
def health():
    return {"status": "running"}
