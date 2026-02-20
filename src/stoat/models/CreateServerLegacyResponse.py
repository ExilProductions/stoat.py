from typing import List, Any
from pydantic import BaseModel

from .Channel import Channel
from .Server import Server

class CreateServerLegacyResponse(BaseModel):
    """Information returned when creating server"""
    server: Server
    channels: List[Channel]