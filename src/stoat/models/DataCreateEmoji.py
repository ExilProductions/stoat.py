from typing import List, Any, Optional
from pydantic import BaseModel

from .EmojiParent import EmojiParent

class DataCreateEmoji(BaseModel):
    """Create a new emoji"""
    name: str
    parent: EmojiParent
    nsfw: Optional[bool]