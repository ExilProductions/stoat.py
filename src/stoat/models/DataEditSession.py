from typing import List, Any
from pydantic import BaseModel


class DataEditSession(BaseModel):
    friendly_name: str