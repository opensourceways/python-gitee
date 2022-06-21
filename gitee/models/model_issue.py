from dataclasses import dataclass, field
from typing import List, Optional

from gitee.models.model_label import Label
from gitee.models.model_milestone import Milestone
from gitee.models.model_program_basic import ProgramBasic
from gitee.models.model_user_basic import UserBasic


@dataclass
class ModelIssue:
    id: Optional[int] = 0
    url: Optional[str] = ""
    repository_url: Optional[str] = ""
    labels_url: Optional[str] = ""
    comments_url: Optional[str] = ""
    html_url: Optional[str] = ""
    parent_url: Optional[str] = ""
    number: Optional[str] = ""
    state: Optional[str] = ""
    title: Optional[str] = ""
    body: Optional[str] = ""
    body_html: Optional[str] = ""
    user: Optional[UserBasic] = UserBasic()
    labels: Optional[List[Label]] = field(default_factory=list)
    assignee: Optional[UserBasic] = UserBasic()
    collaborators: Optional[List[UserBasic]] = field(default_factory=list)
    repository: Optional[str] = ""
    milestone: Optional[Milestone] = Milestone()
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""
    plan_started_at: Optional[str] = ""
    deadline: Optional[str] = ""
    finished_at: Optional[str] = ""
    scheduled_time: Optional[str] = ""
    comments: Optional[int] = 0
    issue_type: Optional[str] = ""
    program: Optional[ProgramBasic] = ProgramBasic()
