from typing import List, Any
from pydantic import BaseModel

from .ServerBan import ServerBan
from .BannedUser import BannedUser

class BanListResult(BaseModel):
    """Ban list result"""
    users: List[BannedUser]
    bans: List[ServerBan]