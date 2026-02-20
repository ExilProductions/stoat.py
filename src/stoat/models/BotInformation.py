from typing import List, Any
from pydantic import BaseModel


class BotInformation(BaseModel):
    """Bot information for if the user is a bot"""
    owner: str