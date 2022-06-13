from dataclasses import dataclass
from typing import Optional


@dataclass
class Milestone:
    url: Optional[str] = ""
    html_url: Optional[str] = ""
    number: Optional[int] = 0
    repository_id: Optional[int] = 0
    state: Optional[str] = ""
    title: Optional[str] = ""
    description: Optional[str] = ""
    updated_at: Optional[str] = ""
    created_at: Optional[str] = ""
    open_issues: Optional[int] = 0
    closed_issues: Optional[int] = 0
    due_on: Optional[str] = ""
