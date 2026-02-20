from typing import List, Any, Optional
from pydantic import BaseModel

from .ReportedContent import ReportedContent

class DataReportContent(BaseModel):
    content: ReportedContent
    additional_context: Optional[str]