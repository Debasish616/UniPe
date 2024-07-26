from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.utils.database import Base

class OTPTransactionsDb(Base):
    __tablename__ = "otp_transactions"
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, index=True)
    code = Column(String)
    created_at = Column(DateTime)
    otp_expires_at = Column(DateTime)
    transaction_expires_at = Column(DateTime)
    is_otp_verified = Column(Boolean, default=False)
    ip_address = Column(String)
