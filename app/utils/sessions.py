import uuid
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session

def create_session(db: Session, user_id: int, ip_address: str):
    session_id = str(uuid.uuid4())
    created_at = datetime.now(timezone.utc)
    expires_at = created_at + timedelta(days=7)  # Session expiry set to 7 days
    session = {
        "session_id": session_id,
        "user_id": user_id,
        "created_at": created_at,
        "expires_at": expires_at,
    }
    # Save session in the database if needed
    return session
