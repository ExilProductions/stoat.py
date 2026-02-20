from typing import List, Any
from pydantic import BaseModel


class DataPermissionsValue(BaseModel):
    """Data permissions Value - contains allow"""
    permissions: int