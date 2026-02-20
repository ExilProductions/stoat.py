from typing import List, Any, Optional
from pydantic import BaseModel

from .ISO8601 Timestamp import ISO8601 Timestamp
from .MemberCompositeKey import MemberCompositeKey
from .File import File

class Member(BaseModel):
    """Server Member"""
    _id: MemberCompositeKey
    joined_at: ISO8601 Timestamp
    nickname: Optional[str]
    avatar: Optional[File]
    roles: Optional[List[str]]
    timeout: Optional[ISO8601 Timestamp]
    can_publish: Optional[bool]
    can_receive: Optional[bool]