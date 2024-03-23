from pydantic import BaseModel, RootModel, field_validator, StringConstraints
from datetime import datetime
from typing import Any, Optional, List, Dict
from utils import date_to_str
from typing_extensions import Annotated

class GroupData(BaseModel):
    group_first_event: Dict = {}
    group_ids: Dict = {}
    path: str
    user_properties_updated: Optional[bool] = False

    class Config:
        populate_by_name = True

    @field_validator('group_first_event','group_ids')
    @classmethod
    def convert_empty_dict(cls, value: dict):
        return {} if value is None else value

class UserProperties(BaseModel):
    initial_li_fat_id: Optional[str] = 'EMPTY'
    initial_rtd_cid: Optional[str] = 'EMPTY'
    user_corporate_id: Optional[int] = None
    user_corporate_is_demo: Optional[bool] = None
    user_corporate_status: Optional[Annotated[str, StringConstraints(to_lower=True)]] = None
    user_role: Optional[str] = None
    user_signup_date: Optional[datetime] = None
    user_status: Optional[str] = None

    class Config:
        populate_by_name = True

class UserEvent(BaseModel):
    date: datetime
    country: Optional[str] = ""
    data: GroupData
    language: Optional[str] = None
    event_type: str
    device_id: str
    server_upload_time: int
    server_received_time: int
    user_id: int
    region: Optional[str] = None
    processed_time: int
    city: Optional[str] = None
    user_properties: UserProperties
    client_event_time: int
    client_upload_time: int
    amp_id: int
    data_type: str
    event_time: int

    class Config:
        from_attributes = True

    @field_validator('city','country')
    @classmethod
    def convert_null_text(cls, value: str):
        if value is not None and value.lower().strip() == 'null':
            return None
        return value

    def dict(self, *args, **kwargs) -> dict:
        return {
            "date": date_to_str(self.date),
            "country": self.country,
            "group_first_event": self.data.group_first_event,
            "group_ids": self.data.group_ids,
            "path": self.data.path,
            "user_properties_updated": self.data.user_properties_updated,
            "language": self.language,
            "event_type": self.event_type,
            "device_id": self.device_id,
            "server_upload_time": self.server_upload_time,
            "server_received_time": self.server_received_time,
            "user_id": self.user_id,
            "region": self.region,
            "processed_time": self.processed_time,
            "city": self.city,
            "initial_li_fat_id": self.user_properties.initial_li_fat_id,
            "initial_rtd_cid": self.user_properties.initial_rtd_cid,
            "user_corporate_id": self.user_properties.user_corporate_id,
            "user_corporate_is_demo": self.user_properties.user_corporate_is_demo,
            "user_corporate_status": self.user_properties.user_corporate_status,
            "user_role": self.user_properties.user_role,
            "user_signup_date": date_to_str(self.user_properties.user_signup_date),
            "user_status": self.user_properties.user_status,
            "client_event_time": self.client_event_time,
            "client_upload_time": self.client_upload_time,
            "amp_id": self.amp_id,
            "data_type": self.data_type,
            "event_time": self.event_time,
        }

class UserEventList(RootModel):
    root: List[UserEvent]
