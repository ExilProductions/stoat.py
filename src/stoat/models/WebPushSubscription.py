from typing import List, Any
from pydantic import BaseModel


class WebPushSubscription(BaseModel):
    """Web Push subscription"""
    endpoint: str
    p256dh: str
    auth: str