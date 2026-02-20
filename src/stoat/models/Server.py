from typing import List, Any, Optional
from pydantic import BaseModel

from .Category import Category
from .ServerRolesModel import ServerRolesModel
from .SystemMessageChannels import SystemMessageChannels
from .File import File

class Server(BaseModel):
    """Server"""
    _id: str
    owner: str
    name: str
    description: Optional[str]
    channels: List[str]
    categories: Optional[List[Category]]
    system_messages: Optional[SystemMessageChannels]
    roles: Optional[ServerRolesModel]
    default_permissions: int
    icon: Optional[File]
    banner: Optional[File]
    flags: Optional[int]
    nsfw: Optional[bool]
    analytics: Optional[bool]
    discoverable: Optional[bool]