from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.enquiry import router as enquiry_router
from app.database import Base, engine, SessionLocal, get_db
from app.models.Enquiry import Enquiry

app = FastAPI(title="We know a broker")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://onsitewash-frontend-app-u7e5k.ondigitalocean.app",
        "https://www.onsitespray.com.au",
        "http://localhost:8080",
        "https://onsitespray.com.au"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(enquiry_router, prefix="/api/v1")


@app.get("/")
def health():
    return {"status": "running"}
