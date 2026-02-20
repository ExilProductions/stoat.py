from typing import List, Any, Optional
from pydantic import BaseModel

from .FieldsBot import FieldsBot

class DataEditBot(BaseModel):
    """New Bot Details"""
    name: Optional[str]
    public: Optional[bool]
    analytics: Optional[bool]
    interactions_url: Optional[str]
    remove: Optional[List[FieldsBot]]