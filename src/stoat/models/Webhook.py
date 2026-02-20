from typing import List, Any, Optional
from pydantic import BaseModel

from .File import File

class Webhook(BaseModel):
    """Webhook"""
    id: str
    name: str
    avatar: Optional[File]
    creator_id: str
    channel_id: str
    permissions: int
    token: Optional[str]