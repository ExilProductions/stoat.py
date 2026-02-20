from typing import List, Any, Optional
from pydantic import BaseModel


class Masquerade(BaseModel):
    """Name and / or avatar override information"""
    name: Optional[str]
    avatar: Optional[str]
    colour: Optional[str]