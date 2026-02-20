from typing import List, Any, Optional
from pydantic import BaseModel

from .User import User

class BotWithUserResponse(BaseModel):
    """Bot with user response"""
    user: User
    _id: str
    owner: str
    token: str
    public: bool
    analytics: Optional[bool]
    discoverable: Optional[bool]
    interactions_url: Optional[str]
    terms_of_service_url: Optional[str]
    privacy_policy_url: Optional[str]
    flags: Optional[int]