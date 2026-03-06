from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.quote import router as quote_router
from app.database import Base, engine, SessionLocal, get_db
from app.models.quote import Quote

app = FastAPI(title="OnsiteWash Backend")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://onsitewash-frontend-app-u7e5k.ondigitalocean.app",
        "https://www.onsitespray.com.au",
        "https://onsitespray.com.au/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quote_router, prefix="/api/v1")


@app.get("/")
def health():
    return {"status": "running"}
