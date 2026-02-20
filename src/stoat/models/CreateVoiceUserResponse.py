from typing import List, Any
from pydantic import BaseModel


class CreateVoiceUserResponse(BaseModel):
    """Voice server token response"""
    token: str
    url: str