from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)

    service_type = Column(String(50), nullable=False)

    preferred_date = Column(String(50), nullable=False)
    preferred_time = Column(String(10), nullable=False)

    additional_notes = Column(String(500), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
