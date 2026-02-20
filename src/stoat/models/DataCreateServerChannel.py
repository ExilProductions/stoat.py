from typing import List, Any, Optional
from pydantic import BaseModel

from .LegacyServerChannelType import LegacyServerChannelType
from .VoiceInformation import VoiceInformation

class DataCreateServerChannel(BaseModel):
    """Create new server channel"""
    type: Optional[LegacyServerChannelType]
    name: str
    description: Optional[str]
    nsfw: Optional[bool]
    voice: Optional[VoiceInformation]