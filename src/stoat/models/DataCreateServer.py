from typing import List, Any, Optional
from pydantic import BaseModel


class DataCreateServer(BaseModel):
    """Information about new server to create"""
    name: str
    description: Optional[str]
    nsfw: Optional[bool]