from typing import List, Any
from pydantic import BaseModel

from .Override import Override

class DataSetRolePermissions(BaseModel):
    """New role permissions"""
    permissions: Override