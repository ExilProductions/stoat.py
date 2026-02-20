from typing import List, Any, Optional
from pydantic import BaseModel


class ReplyIntent(BaseModel):
    """What this message should reply to and how"""
    id: str
    mention: bool
    fail_if_not_exists: Optional[bool]