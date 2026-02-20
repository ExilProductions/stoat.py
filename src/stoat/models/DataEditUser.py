from typing import List, Any, Optional
from pydantic import BaseModel

from .FieldsUser import FieldsUser
from .DataUserProfile import DataUserProfile
from .UserStatus import UserStatus

class DataEditUser(BaseModel):
    """New user information"""
    display_name: Optional[str]
    avatar: Optional[str]
    status: Optional[UserStatus]
    profile: Optional[DataUserProfile]
    badges: Optional[int]
    flags: Optional[int]
    remove: Optional[List[FieldsUser]]