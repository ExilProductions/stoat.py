from typing import List, Any, Optional
from pydantic import BaseModel


class DataUserProfile(BaseModel):
    """New user profile data"""
    content: Optional[str]
    background: Optional[str]