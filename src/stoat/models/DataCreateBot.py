from typing import List, Any
from pydantic import BaseModel


class DataCreateBot(BaseModel):
    """Bot Details"""
    name: str