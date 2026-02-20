from typing import List, Any, Optional
from pydantic import BaseModel

from .EmojiParent import EmojiParent

class Emoji(BaseModel):
    """Emoji"""
    _id: str
    parent: EmojiParent
    creator_id: str
    name: str
    animated: Optional[bool]
    nsfw: Optional[bool]