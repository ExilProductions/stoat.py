from typing import List, Any, Optional
from pydantic import BaseModel

from .Masquerade import Masquerade
from .Interactions import Interactions
from .ReplyIntent import ReplyIntent
from .SendableEmbed import SendableEmbed

class DataMessageSend(BaseModel):
    """Message to send"""
    nonce: Optional[str]
    content: Optional[str]
    attachments: Optional[List[str]]
    replies: Optional[List[ReplyIntent]]
    embeds: Optional[List[SendableEmbed]]
    masquerade: Optional[Masquerade]
    interactions: Optional[Interactions]
    flags: Optional[int]