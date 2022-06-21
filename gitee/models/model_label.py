from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelLabel:
    id: Optional[int] = 0
    name: Optional[str] = ""
    color: Optional[str] = ""
    repository_id: Optional[int] = 0
    url: Optional[str] = ""
