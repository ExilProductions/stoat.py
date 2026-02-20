from typing import List, Any
from pydantic import BaseModel

from .VoiceNode import VoiceNode

class VoiceFeature(BaseModel):
    enabled: bool
    nodes: List[VoiceNode]