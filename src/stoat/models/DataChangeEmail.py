from typing import List, Any
from pydantic import BaseModel


class DataChangeEmail(BaseModel):
    email: str
    current_password: str