from typing import List, Any, Optional
from pydantic import BaseModel


class SendableEmbed(BaseModel):
    """Representation of a text embed before it is sent."""
    icon_url: Optional[str]
    url: Optional[str]
    title: Optional[str]
    description: Optional[str]
    media: Optional[str]
    colour: Optional[str]