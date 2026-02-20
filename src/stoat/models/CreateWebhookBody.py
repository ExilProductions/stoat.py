from typing import List, Any, Optional
from pydantic import BaseModel


class CreateWebhookBody(BaseModel):
    """Information for the webhook"""
    name: str
    avatar: Optional[str]