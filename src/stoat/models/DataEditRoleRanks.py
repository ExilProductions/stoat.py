from typing import List, Any
from pydantic import BaseModel


class DataEditRoleRanks(BaseModel):
    """New role positions"""
    ranks: List[str]