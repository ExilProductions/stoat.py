from typing import List, Any, Optional
from pydantic import BaseModel


class VoiceInformation(BaseModel):
    """Voice information for a channel"""
    max_users: Optional[int]