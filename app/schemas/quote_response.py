from pydantic import BaseModel
from datetime import datetime


class QuoteResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    email: str
    address: str
    service_type: str
    preferred_date: str
    preferred_time: str
    additional_notes: str | None
    created_at: datetime

    class Config:
        from_attributes = True
