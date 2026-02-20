from typing import List, Any
from pydantic import BaseModel


class DataOnboard(BaseModel):
    username: str