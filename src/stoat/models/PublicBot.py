from typing import List, Any, Optional
from pydantic import BaseModel


class PublicBot(BaseModel):
    """Public Bot"""
    _id: str
    username: str
    avatar: Optional[str]
    description: Optional[str]