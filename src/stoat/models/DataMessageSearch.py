from typing import List, Any, Optional
from pydantic import BaseModel

from .MessageSort import MessageSort

class DataMessageSearch(BaseModel):
    """Options for searching for messages"""
    query: Optional[str]
    pinned: Optional[bool]
    limit: Optional[int]
    before: Optional[str]
    after: Optional[str]
    sort: Optional[MessageSort]
    include_users: Optional[bool]