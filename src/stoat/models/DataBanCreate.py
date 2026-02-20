from typing import List, Any, Optional
from pydantic import BaseModel


class DataBanCreate(BaseModel):
    """Information for new server ban"""
    reason: Optional[str]