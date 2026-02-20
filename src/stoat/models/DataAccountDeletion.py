from typing import List, Any
from pydantic import BaseModel


class DataAccountDeletion(BaseModel):
    token: str