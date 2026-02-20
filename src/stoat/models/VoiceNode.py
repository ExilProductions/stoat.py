from typing import List, Any
from pydantic import BaseModel


class VoiceNode(BaseModel):
    name: str
    lat: float
    lon: float
    public_url: str