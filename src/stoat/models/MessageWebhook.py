from typing import List, Any, Optional
from pydantic import BaseModel


class MessageWebhook(BaseModel):
    """Information about the webhook bundled with Message"""
    name: str
    avatar: Optional[str]