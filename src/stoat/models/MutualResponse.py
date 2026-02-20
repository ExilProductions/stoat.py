from typing import List, Any
from pydantic import BaseModel


class MutualResponse(BaseModel):
    """Mutual friends, servers, groups and DMs response"""
    users: List[str]
    servers: List[str]
    channels: List[str]