from typing import List, Any
from pydantic import BaseModel

from build.BuildInformation import BuildInformation
from .RevoltFeatures import RevoltFeatures

class RevoltConfig(BaseModel):
    revolt: str
    features: RevoltFeatures
    ws: str
    app: str
    vapid: str
    build: BuildInformation