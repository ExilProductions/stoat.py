from typing import List, Any
from pydantic import BaseModel

from .RelationshipStatus import RelationshipStatus

class Relationship(BaseModel):
    """Relationship entry indicating current status with other user"""
    _id: str
    status: RelationshipStatus