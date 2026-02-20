from typing import List, Any, Optional
from pydantic import BaseModel


class DataSendPasswordReset(BaseModel):
    email: str
    captcha: Optional[str]