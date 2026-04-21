from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.enquiry import EnquiryRequest, EnquiryResponse
from app.database import SessionLocal
from app.models.Enquiry import Enquiry
from app.services.email_service import send_email

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
@router.post("/enquiries")
def create_enquiry(request: EnquiryRequest, db: Session = Depends(get_db)):

    db_enquiry = Enquiry(
        full_name=request.full_name,
        email=request.email,
        phone=request.phone,
        service=request.service,
        message=request.message,
    )

    db.add(db_enquiry)
    db.commit()
    db.refresh(db_enquiry)

    # 📧 Email context
    context = {
        "full_name": request.full_name,
        "email": request.email,
        "phone": request.phone,
        "service": request.service,
        "message": request.message,
    }

    # 📧 Send Email
    try:
        send_email(
            request.email,
            "WeKnowABroker - Enquiry Received",
            "enquiry_owner.html",
            context
        )
    except Exception as e:
        print("Email sending failed:", e)

    return {"id": db_enquiry.id}


# =========================
# READ ALL
# =========================
@router.get("/enquiries", response_model=List[EnquiryResponse])
def get_all_enquiries(db: Session = Depends(get_db)):
    return db.query(Enquiry).all()


# =========================
# READ ONE
# =========================
@router.get("/enquiries/{enquiry_id}", response_model=EnquiryResponse)
def get_enquiry(enquiry_id: int, db: Session = Depends(get_db)):

    enquiry = db.query(Enquiry).filter(Enquiry.id == enquiry_id).first()

    if not enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")

    return enquiry


# =========================
# UPDATE
# =========================
@router.put("/enquiries/{enquiry_id}")
def update_enquiry(enquiry_id: int, request: EnquiryRequest, db: Session = Depends(get_db)):

    enquiry = db.query(Enquiry).filter(Enquiry.id == enquiry_id).first()

    if not enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")

    enquiry.full_name = request.full_name
    enquiry.email = request.email
    enquiry.phone = request.phone
    enquiry.service = request.service
    enquiry.message = request.message

    db.commit()
    db.refresh(enquiry)

    return {"message": "Enquiry updated successfully"}


# =========================
# DELETE
# =========================
@router.delete("/enquiries/{enquiry_id}")
def delete_enquiry(enquiry_id: int, db: Session = Depends(get_db)):

    enquiry = db.query(Enquiry).filter(Enquiry.id == enquiry_id).first()

    if not enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")

    db.delete(enquiry)
    db.commit()

    return {"message": "Enquiry deleted successfully"}
