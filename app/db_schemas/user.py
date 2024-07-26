from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.utils.database import Base

class UserDb(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    password_hash = Column(String)
    password_salt = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(DateTime)
    gender = Column(String)
    created_at = Column(DateTime)
