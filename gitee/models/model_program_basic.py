from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelProgramBasic:
    id: Optional[str] = ""
    name: Optional[str] = ""
    description: Optional[str] = ""
    assignee: Optional[str] = ""
    author: Optional[str] = ""
