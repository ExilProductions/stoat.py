from typing import List, Any, Optional
from pydantic import BaseModel


class SystemMessageChannels(BaseModel):
    """System message channel assignments"""
    user_joined: Optional[str]
    user_left: Optional[str]
    user_kicked: Optional[str]
    user_banned: Optional[str]