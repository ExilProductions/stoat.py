from typing import List, Any, Optional
from pydantic import BaseModel


class ResponseWebhook(BaseModel):
    """Webhook information"""
    id: str
    name: str
    avatar: Optional[str]
    channel_id: str
    permissions: int