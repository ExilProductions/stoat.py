from typing import List, Any
from pydantic import BaseModel

from .User import User
from .Member import Member

class AllMemberResponse(BaseModel):
    """Response with all members"""
    members: List[Member]
    users: List[User]