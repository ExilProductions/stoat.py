from typing import List, Any
from pydantic import BaseModel


class Override(BaseModel):
    """Representation of a single permission override"""
    allow: int
    deny: int