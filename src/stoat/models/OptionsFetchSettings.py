from typing import List, Any
from pydantic import BaseModel


class OptionsFetchSettings(BaseModel):
    """Options for fetching settings"""
    keys: List[str]