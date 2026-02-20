from typing import List, Any
from pydantic import BaseModel


class DataHello(BaseModel):
    onboarding: bool