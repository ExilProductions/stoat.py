from typing import List, Any
from pydantic import BaseModel


class CaptchaFeature(BaseModel):
    enabled: bool
    key: str