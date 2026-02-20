from typing import List, Any, Optional
from pydantic import BaseModel

from .Presence import Presence

class UserStatus(BaseModel):
    """User's active status"""
    text: Optional[str]
    presence: Optional[Presence]