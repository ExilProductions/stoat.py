from typing import List, Any
from pydantic import BaseModel


class AccountInfo(BaseModel):
    _id: str
    email: str