from typing import List, Any, Optional
from pydantic import BaseModel

from .SendableEmbed import SendableEmbed

class DataEditMessage(BaseModel):
    """Changes to make to message"""
    content: Optional[str]
    embeds: Optional[List[SendableEmbed]]