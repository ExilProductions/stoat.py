from typing import List, Any
from pydantic import BaseModel


class OverrideField(BaseModel):
    """Representation of a single permission override as it appears on models and in the database"""
    a: int
    d: int