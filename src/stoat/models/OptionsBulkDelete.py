from typing import List, Any
from pydantic import BaseModel


class OptionsBulkDelete(BaseModel):
    """Options for bulk deleting messages"""
    ids: List[str]