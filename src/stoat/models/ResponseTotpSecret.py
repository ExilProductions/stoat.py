from typing import List, Any
from pydantic import BaseModel


class ResponseTotpSecret(BaseModel):
    secret: str