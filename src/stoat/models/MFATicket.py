from typing import List, Any, Optional
from pydantic import BaseModel


class MFATicket(BaseModel):
    """Multi-factor auth ticket"""
    _id: str
    account_id: str
    token: str
    validated: bool
    authorised: bool
    last_totp_code: Optional[str]