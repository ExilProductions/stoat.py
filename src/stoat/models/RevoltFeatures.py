from typing import List, Any
from pydantic import BaseModel

from .VoiceFeature import VoiceFeature
from .CaptchaFeature import CaptchaFeature
from .Feature import Feature

class RevoltFeatures(BaseModel):
    captcha: CaptchaFeature
    email: bool
    invite_only: bool
    autumn: Feature
    january: Feature
    livekit: VoiceFeature