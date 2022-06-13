from dataclasses import dataclass
from typing import Optional


@dataclass
class Label:
    id: Optional[int] = 0
    name: Optional[str] = ""
    color: Optional[str] = ""
    repository_id: Optional[int] = 0
    url: Optional[str] = ""
