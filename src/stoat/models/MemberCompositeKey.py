from typing import List, Any
from pydantic import BaseModel


class MemberCompositeKey(BaseModel):
    """Composite primary key consisting of server and user id"""
    server: str
    user: str