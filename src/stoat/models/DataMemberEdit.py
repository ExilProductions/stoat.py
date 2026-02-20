from typing import List, Any, Optional
from pydantic import BaseModel

from .ISO8601 Timestamp import ISO8601 Timestamp
from .FieldsMember import FieldsMember

class DataMemberEdit(BaseModel):
    """New member information"""
    nickname: Optional[str]
    avatar: Optional[str]
    roles: Optional[List[str]]
    timeout: Optional[ISO8601 Timestamp]
    can_publish: Optional[bool]
    can_receive: Optional[bool]
    voice_channel: Optional[str]
    remove: Optional[List[FieldsMember]]