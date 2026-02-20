from typing import List, Any
from pydantic import BaseModel


class BuildInformation(BaseModel):
    commit_sha: str
    commit_timestamp: str
    semver: str
    origin_url: str
    timestamp: str