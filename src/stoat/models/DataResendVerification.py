from typing import List, Any, Optional
from pydantic import BaseModel


class DataResendVerification(BaseModel):
    email: str
    captcha: Optional[str]