from typing import List, Any, Optional
from pydantic import BaseModel

from .ChannelCompositeKey import ChannelCompositeKey

class ChannelUnread(BaseModel):
    """Channel Unread"""
    _id: ChannelCompositeKey
    last_id: Optional[str]
    mentions: Optional[List[str]]