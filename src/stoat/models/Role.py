from typing import List, Any, Optional
from pydantic import BaseModel

from .OverrideField import OverrideField

class Role(BaseModel):
    """Role"""
    _id: str
    name: str
    permissions: OverrideField
    colour: Optional[str]
    hoist: Optional[bool]
    rank: Optional[int]