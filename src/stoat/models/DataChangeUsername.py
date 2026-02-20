from typing import List, Any
from pydantic import BaseModel


class DataChangeUsername(BaseModel):
    username: str
    password: str