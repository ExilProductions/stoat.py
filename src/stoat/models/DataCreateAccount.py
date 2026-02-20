from typing import List, Any, Optional
from pydantic import BaseModel


class DataCreateAccount(BaseModel):
    email: str
    password: str
    invite: Optional[str]
    captcha: Optional[str]