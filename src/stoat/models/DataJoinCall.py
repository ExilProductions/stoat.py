from typing import List, Any, Optional
from pydantic import BaseModel


class DataJoinCall(BaseModel):
    """Join a voice channel"""
    node: Optional[str]
    force_disconnect: Optional[bool]
    recipients: Optional[List[str]]