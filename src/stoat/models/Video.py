from typing import List, Any
from pydantic import BaseModel


class Video(BaseModel):
    """Video"""
    url: str
    width: int
    height: int