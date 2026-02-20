from typing import List, Any
from pydantic import BaseModel

from .User import User
from .Bot import Bot

class OwnedBotsResponse(BaseModel):
    """Owned Bots Response

Both lists are sorted by their IDs.

TODO: user should be in bot object"""
    bots: List[Bot]
    users: List[User]