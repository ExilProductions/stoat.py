from typing import List, Any
from pydantic import BaseModel

from .User import User
from .Bot import Bot

class FetchBotResponse(BaseModel):
    """Bot Response"""
    bot: Bot
    user: User