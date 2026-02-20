from typing import List, Any
from pydantic import BaseModel


class SessionInfo(BaseModel):
    _id: str
    name: str