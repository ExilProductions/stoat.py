from typing import List, Any, Optional
from pydantic import BaseModel


class DataCreateRole(BaseModel):
    """Information about new role to create"""
    name: str
    rank: Optional[int]