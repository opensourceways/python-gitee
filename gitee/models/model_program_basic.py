from dataclasses import dataclass
from typing import Optional


@dataclass
class ProgramBasic:
    id: Optional[str] = ""
    name: Optional[str] = ""
    description: Optional[str] = ""
    assignee: Optional[str] = ""
    author: Optional[str] = ""
