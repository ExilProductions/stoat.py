from typing import List, Any
from pydantic import BaseModel


class MultiFactorStatus(BaseModel):
    email_otp: bool
    trusted_handover: bool
    email_mfa: bool
    totp_mfa: bool
    security_key_mfa: bool
    recovery_active: bool