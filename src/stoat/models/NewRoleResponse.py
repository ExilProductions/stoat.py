from typing import List, Any
from pydantic import BaseModel

from .Role import Role

class NewRoleResponse(BaseModel):
    """Response after creating new role"""
    id: str
    role: Role