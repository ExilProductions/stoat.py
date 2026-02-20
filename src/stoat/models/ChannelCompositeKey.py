from typing import List, Any
from pydantic import BaseModel


class ChannelCompositeKey(BaseModel):
    """Composite primary key consisting of channel and user id"""
    channel: str
    user: str