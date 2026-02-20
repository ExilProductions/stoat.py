from typing import List, Any, Optional
from pydantic import BaseModel

from .File import File

class UserProfile(BaseModel):
    """User's profile"""
    content: Optional[str]
    background: Optional[File]