from typing import List, Any, Optional
from pydantic import BaseModel


class DataCreateGroup(BaseModel):
    """Create new group"""
    name: str
    description: Optional[str]
    icon: Optional[str]
    users: Optional[List[str]]
    nsfw: Optional[bool]