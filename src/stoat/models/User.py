from typing import List, Any, Optional
from pydantic import BaseModel

from .UserStatus import UserStatus
from .Relationship import Relationship
from .BotInformation import BotInformation
from .RelationshipStatus import RelationshipStatus
from .File import File

class User(BaseModel):
    """User"""
    _id: str
    username: str
    discriminator: str
    display_name: Optional[str]
    avatar: Optional[File]
    relations: Optional[List[Relationship]]
    badges: Optional[int]
    status: Optional[UserStatus]
    flags: Optional[int]
    privileged: Optional[bool]
    bot: Optional[BotInformation]
    relationship: RelationshipStatus
    online: bool