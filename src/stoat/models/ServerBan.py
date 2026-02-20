from typing import List, Any, Optional
from pydantic import BaseModel

from .MemberCompositeKey import MemberCompositeKey

class ServerBan(BaseModel):
    """Server Ban"""
    _id: MemberCompositeKey
    reason: Optional[str]