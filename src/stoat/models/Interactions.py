from typing import List, Any, Optional
from pydantic import BaseModel


class Interactions(BaseModel):
    """Information to guide interactions on this message"""
    reactions: Optional[List[str]]
    restrict_reactions: Optional[bool]