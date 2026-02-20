from typing import List, Any, Optional
from pydantic import BaseModel

from .File import File

class BannedUser(BaseModel):
    """Just enough information to list a ban"""
    _id: str
    username: str
    discriminator: str
    avatar: Optional[File]