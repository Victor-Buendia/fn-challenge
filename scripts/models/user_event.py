from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, Boolean, DateTime, PrimaryKeyConstraint, Integer, BigInteger, Uuid
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

Base = declarative_base()

class UserEvent(Base):
    __tablename__ = "user_events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    inserted_at_utc = Column(DateTime, default=datetime.utcnow)
    amp_id = Column(BigInteger)
    city = Column(String(250))
    client_event_time = Column(BigInteger)
    client_upload_time = Column(BigInteger)
    country = Column(String(250))
    data_type = Column(String(250))
    date = Column(DateTime)
    device_id = Column(String(250))
    event_time = Column(BigInteger)
    event_type = Column(String(250))
    group_first_event = Column(JSONB)
    group_ids = Column(JSONB)
    initial_li_fat_id = Column(String(250))
    initial_rtd_cid = Column(String(250))
    language = Column(String(250))
    path = Column(String(250))
    processed_time = Column(BigInteger)
    region = Column(String(250))
    server_received_time = Column(BigInteger)
    server_upload_time = Column(BigInteger)
    user_corporate_id = Column(BigInteger)
    user_corporate_is_demo = Column(Boolean)
    user_corporate_status = Column(String(250))
    user_id = Column(BigInteger)
    user_properties_updated = Column(Boolean)
    user_role = Column(String(250))
    user_signup_date = Column(DateTime)
    user_status = Column(String(250))

    # __table_args__ = (PrimaryKeyConstraint("user_id", "processed_time"),)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}