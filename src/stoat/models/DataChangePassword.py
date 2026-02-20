from typing import List, Any
from pydantic import BaseModel


class DataChangePassword(BaseModel):
    password: str
    current_password: str