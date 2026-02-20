from typing import List, Any, Optional
from pydantic import BaseModel

from .FieldsRole import FieldsRole

class DataEditRole(BaseModel):
    """New role information"""
    name: Optional[str]
    colour: Optional[str]
    hoist: Optional[bool]
    rank: Optional[int]
    remove: Optional[List[FieldsRole]]