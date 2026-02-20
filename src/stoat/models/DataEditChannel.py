from typing import List, Any, Optional
from pydantic import BaseModel

from .VoiceInformation import VoiceInformation
from .FieldsChannel import FieldsChannel

class DataEditChannel(BaseModel):
    """New webhook information"""
    name: Optional[str]
    description: Optional[str]
    owner: Optional[str]
    icon: Optional[str]
    nsfw: Optional[bool]
    archived: Optional[bool]
    voice: Optional[VoiceInformation]
    remove: Optional[List[FieldsChannel]]