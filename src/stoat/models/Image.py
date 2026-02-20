from typing import List, Any
from pydantic import BaseModel

from .ImageSize import ImageSize

class Image(BaseModel):
    """Image"""
    url: str
    width: int
    height: int
    size: ImageSize