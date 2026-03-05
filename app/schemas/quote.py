from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date
from enum import Enum
from typing import Optional
import re


class ServiceType(str, Enum):
    truck_wash = "Truck Wash"
    fleet_wash = "Fleet Wash"
    commercial_dock_wash = "Commercial Dock Wash"
    pressure_washing = "Pressure Washing"


class QuoteRequest(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=6, max_length=20)
    email: EmailStr
    address: str = Field(..., min_length=5, max_length=200)

    service_type: ServiceType
    preferred_date: date
    preferred_time: str

    additional_notes: Optional[str] = Field(None, max_length=500)

    @field_validator("preferred_time")
    @classmethod
    def validate_time_format(cls, v: str):
        pattern = r"^(0?[1-9]|1[0-2]):[0-5][0-9] (AM|PM)$"
        if not re.match(pattern, v):
            raise ValueError("Time must be in format 'HH:MM AM/PM'")
        return v

    class Config:
        from_attributes = True
