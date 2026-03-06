from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.quote import QuoteRequest
from app.schemas.quote_response import QuoteResponse

from app.database import SessionLocal
from app.models.quote import Quote
from app.services.email_service import send_email
import os

router = APIRouter()

# -------------------------
# Database Dependency
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# CREATE
# =========================
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
        "phone": request.phone,
        "email": request.email,
        "service_type": request.service_type.value,
        "preferred_date": request.preferred_date,
        "preferred_time": request.preferred_time,
        "additional_notes": request.additional_notes,
    }

    try:
        send_email(
            request.email,
            "OnsiteWash - Quote Confirmation",
            "quote_owner.html",
            context
        )
    except Exception as e:
        print("Email sending failed:", e)

   
    return {"id": db_quote.id}


# =========================
# READ ALL
# =========================
@router.get("/quotes", response_model=List[QuoteRequest])
def get_all_quotes(db: Session = Depends(get_db)):
    quotes = db.query(Quote).all()
    return quotes


# =========================
# READ ONE
# =========================
@router.get("/quotes/{quote_id}")
def get_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = db.query(Quote).filter(Quote.id == quote_id).first()

    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")

    return quote


# =========================
# UPDATE
# =========================
@router.put("/quotes/{quote_id}")
def update_quote(quote_id: int, request: QuoteRequest, db: Session = Depends(get_db)):

    quote = db.query(Quote).filter(Quote.id == quote_id).first()

    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")

    quote.full_name = request.full_name
    quote.phone = request.phone
    quote.email = request.email
    quote.address = request.address
    quote.service_type = request.service_type
    quote.preferred_date = str(request.preferred_date)
    quote.preferred_time = request.preferred_time
    quote.additional_notes = request.additional_notes

    db.commit()
    db.refresh(quote)

    return {"message": "Quote updated successfully"}


# =========================
# DELETE
# =========================
@router.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):

    quote = db.query(Quote).filter(Quote.id == quote_id).first()

    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")

    db.delete(quote)
    db.commit()

    return {"message": "Quote deleted successfully"}
