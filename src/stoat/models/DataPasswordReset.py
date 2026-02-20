from typing import List, Any, Optional
from pydantic import BaseModel


class DataPasswordReset(BaseModel):
    token: str
    password: str
    remove_sessions: Optional[bool]