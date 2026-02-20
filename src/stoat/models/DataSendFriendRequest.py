from typing import List, Any
from pydantic import BaseModel


class DataSendFriendRequest(BaseModel):
    """User lookup information"""
    username: str