from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.quote import QuoteRequest
from app.database import SessionLocal
from app.models.quote import Quote
from app.services.email_service import send_email
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/quotes")
def create_quote(request: QuoteRequest, db: Session = Depends(get_db)):

    db_quote = Quote(
        full_name=request.full_name,
        phone=request.phone,
        email=request.email,
        address=request.address,
        service_type=request.service_type,
        preferred_date=str(request.preferred_date),
        preferred_time=request.preferred_time,
        additional_notes=request.additional_notes,
    )

    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)

    context = {
    "full_name": request.full_name,
    "service_type": request.service_type,
    "preferred_date": request.preferred_date,
    "preferred_time": request.preferred_time,
    "email": request.email,
    "phone": request.phone
}

    # email to customer
    send_email(
        request.email,
        "OnsiteWash - Quote Confirmation",
        "quote_customer.html",
        context
    )

    # email to owner
    send_email(
        os.getenv("OWNER_EMAIL"),
        "New Quote Request",
        "quote_owner.html",
        context
    )


    return {"id": db_quote.id}
