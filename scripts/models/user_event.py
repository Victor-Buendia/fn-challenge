from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, Boolean, DateTime, PrimaryKeyConstraint, Integer, BigInteger, Uuid
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime


Base = declarative_base()

class UserEvent(Base):
    __tablename__ = "user_events"
    inserted_at_utc = Column(DateTime, default=datetime.utcnow)
    amp_id = Column(BigInteger)
    city = Column(String(120))
    client_event_time = Column(BigInteger)
    client_upload_time = Column(BigInteger)
    country = Column(String(120))
    data_type = Column(String(100))
    date = Column(DateTime)
    device_id = Column(String(36), primary_key=True)
    event_time = Column(BigInteger, primary_key=True)
    event_type = Column(String(120))
    group_first_event = Column(JSONB)
    group_ids = Column(JSONB)
    initial_li_fat_id = Column(String(120))
    initial_rtd_cid = Column(String(120))
    language = Column(String(120))
    path = Column(String(120))
    processed_time = Column(BigInteger)
    region = Column(String(120))
    server_received_time = Column(BigInteger)
    server_upload_time = Column(BigInteger)
    user_corporate_id = Column(BigInteger)
    user_corporate_is_demo = Column(Boolean)
    user_corporate_status = Column(String(50))
    user_id = Column(BigInteger)
    user_properties_updated = Column(Boolean)
    user_role = Column(String(120))
    user_signup_date = Column(DateTime)
    user_status = Column(String(50))

    __table_args__ = (PrimaryKeyConstraint("device_id", "event_time"),)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}