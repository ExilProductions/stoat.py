from typing import List, Any, Optional
from pydantic import BaseModel

from .FieldsWebhook import FieldsWebhook

class DataEditWebhook(BaseModel):
    """New webhook information"""
    name: Optional[str]
    avatar: Optional[str]
    permissions: Optional[int]
    remove: Optional[List[FieldsWebhook]]