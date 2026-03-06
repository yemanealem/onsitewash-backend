from pydantic import BaseModel
from typing import Optional
from datetime import date


class QuoteUpdate(BaseModel):

    full_name: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    address: Optional[str]

    service_type: Optional[str]
    preferred_date: Optional[date]
    preferred_time: Optional[str]

    additional_notes: Optional[str]
