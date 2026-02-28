from pydantic import BaseModel, EmailStr, Field
from datetime import date
from enum import Enum
from typing import Optional

class ServiceType(str, Enum):
    basic = "basic"
    premium = "premium"
    deluxe = "deluxe"

class PreferredTime(str, Enum):
    AM = "AM"
    PM = "PM"

class QuoteRequest(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=6, max_length=20)
    email: EmailStr
    address: str = Field(..., min_length=5, max_length=200)

    service_type: ServiceType
    preferred_date: date
    preferred_time: PreferredTime

    additional_notes: Optional[str] = Field(None, max_length=500)

    class Config:
        orm_mode = True
