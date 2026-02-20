from typing import List, Any, Optional
from pydantic import BaseModel

from .Metadata import Metadata

class File(BaseModel):
    """File"""
    _id: str
    tag: str
    filename: str
    metadata: Metadata
    content_type: str
    size: int
    deleted: Optional[bool]
    reported: Optional[bool]
    message_id: Optional[str]
    user_id: Optional[str]
    server_id: Optional[str]
    object_id: Optional[str]