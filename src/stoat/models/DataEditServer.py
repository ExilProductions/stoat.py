from typing import List, Any, Optional
from pydantic import BaseModel

from .Category import Category
from .SystemMessageChannels import SystemMessageChannels
from .FieldsServer import FieldsServer

class DataEditServer(BaseModel):
    """New server information"""
    name: Optional[str]
    description: Optional[str]
    icon: Optional[str]
    banner: Optional[str]
    categories: Optional[List[Category]]
    system_messages: Optional[SystemMessageChannels]
    flags: Optional[int]
    discoverable: Optional[bool]
    analytics: Optional[bool]
    remove: Optional[List[FieldsServer]]