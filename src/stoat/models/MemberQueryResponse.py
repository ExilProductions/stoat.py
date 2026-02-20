from typing import List, Any
from pydantic import BaseModel

from .User import User
from .Member import Member

class MemberQueryResponse(BaseModel):
    members: List[Member]
    users: List[User]