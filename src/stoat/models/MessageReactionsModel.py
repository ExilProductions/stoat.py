from typing import List, Any
from pydantic import BaseModel


class MessageReactionsModel(BaseModel):
    """Hashmap of emoji IDs to array of user IDs"""
    pass