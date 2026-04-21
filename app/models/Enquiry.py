from sqlalchemy import Column, Integer, String, Text
from app.database import Base
class Enquiry(Base):
    __tablename__ = "enquiries"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    service = Column(String)
    message = Column(Text, nullable=False)
