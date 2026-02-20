from typing import List, Any
from pydantic import BaseModel


class Category(BaseModel):
    """Channel category"""
    id: str
    title: str
    channels: List[str]