from pydantic import BaseModel, EmailStr
from typing import Optional
from app.enums.service_type import ServiceType


class EnquiryRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    service: ServiceType
    message: str


class EnquiryResponse(EnquiryRequest):
    id: int

    class Config:
        from_attributes = True
