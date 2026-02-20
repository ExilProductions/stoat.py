from typing import List, Any, Optional
from pydantic import BaseModel

from .ISO8601 Timestamp import ISO8601 Timestamp
from .User import User
from .MessageWebhook import MessageWebhook
from .MessageReactionsModel import MessageReactionsModel
from .Masquerade import Masquerade
from .SystemMessage import SystemMessage
from .Member import Member
from .Interactions import Interactions
from .Embed import Embed
from .File import File

class Message(BaseModel):
    """Message"""
    _id: str
    nonce: Optional[str]
    channel: str
    author: str
    user: Optional[User]
    member: Optional[Member]
    webhook: Optional[MessageWebhook]
    content: Optional[str]
    system: Optional[SystemMessage]
    attachments: Optional[List[File]]
    edited: Optional[ISO8601 Timestamp]
    embeds: Optional[List[Embed]]
    mentions: Optional[List[str]]
    role_mentions: Optional[List[str]]
    replies: Optional[List[str]]
    reactions: Optional[MessageReactionsModel]
    interactions: Optional[Interactions]
    masquerade: Optional[Masquerade]
    pinned: Optional[bool]
    flags: Optional[int]