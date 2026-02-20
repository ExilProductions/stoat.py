from typing import List, Any
from pydantic import BaseModel


class Feature(BaseModel):
    enabled: bool
    url: str