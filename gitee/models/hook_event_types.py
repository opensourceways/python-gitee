from dataclasses import dataclass, field
from typing import List, Optional

from gitee.models.hook_event_models import *


@dataclass
class NoteEvent(object):
    action: Optional[str] = ""
    comment: Optional[NoteHook] = NoteHook()
    repository: Optional[ProjectHook] = ProjectHook()
    project: Optional[ProjectHook] = ProjectHook()
    author: Optional[UserHook] = UserHook()
    sender: Optional[UserHook] = UserHook()
    url: Optional[str] = ""
    note: Optional[str] = ""
    noteable_type: Optional[str] = ""
    noteable_id: Optional[str] = ""
    title: Optional[str] = ""
    per_iid: Optional[str] = ""
    short_commit_id: Optional[str] = ""
    enterprise: Optional[EnterpriseHook] = EnterpriseHook()
    pull_request: Optional[PullRequestHook] = PullRequestHook()
    issue: Optional[IssueHook] = IssueHook()
    hook_name: Optional[str] = ""
    password: Optional[str] = ""


@dataclass
class IssueEvent:
    action: Optional[str] = ""
    issue: Optional[IssueHook] = IssueHook()
    repository: Optional[ProjectHook] = ProjectHook()
    project: Optional[ProjectHook] = ProjectHook()
    sender: Optional[UserHook] = UserHook()
    target_user: Optional[UserHook] = UserHook()
    user: Optional[UserHook] = UserHook()
    assignee: Optional[UserHook] = UserHook()
    updated_by: Optional[UserHook] = UserHook()
    iid: Optional[str] = ""
    title: Optional[str] = ""
    description: Optional[str] = ""
    state: Optional[str] = ""
    milestone: Optional[str] = ""
    url: Optional[str] = ""
    enterprise: Optional[EnterpriseHook] = EnterpriseHook()
    hook_name: Optional[str] = ""
    password: Optional[str] = ""


@dataclass
class RepoInfo:
    project: Optional[ProjectHook] = ProjectHook()
    repository: Optional[ProjectHook] = ProjectHook


@dataclass
class PullRequestEvent:
    action: Optional[str] = ""
    action_desc: Optional[str] = ""
    pull_request: Optional[PullRequestHook] = PullRequestHook()
    number: Optional[int] = 0
    iid: Optional[int] = 0
    title: Optional[str] = ""
    body: Optional[str] = ""
    state: Optional[str] = ""
    merge_status: Optional[str] = ""
    merge_commit_sha: Optional[str] = ""
    url: Optional[str] = ""
    source_branch: Optional[str] = ""
    source_repo: Optional[RepoInfo] = RepoInfo()
    target_branch: Optional[str] = ""
    target_repo: Optional[RepoInfo] = RepoInfo()
    project: Optional[ProjectHook] = ProjectHook()
    repository: Optional[ProjectHook] = ProjectHook()
    author: Optional[UserHook] = UserHook()
    updated_by: Optional[UserHook] = UserHook()
    sender: Optional[UserHook] = UserHook()
    target_user: Optional[UserHook] = UserHook()
    enterprise: Optional[EnterpriseHook] = EnterpriseHook()
    hook_name: Optional[str] = ""
    password: Optional[str] = ""


@dataclass
class PushEvent:
    ref: Optional[str] = ""
    before: Optional[str] = ""
    after: Optional[str] = ""
    total_commits_count: Optional[int] = 0
    commits_more_than_ten: Optional[bool] = False
    created: Optional[bool] = False
    deleted: Optional[bool] = False
    compare: Optional[str] = ""
    commits: Optional[List[CommitHook]] = field(default_factory=list)
    head_commit: Optional[CommitHook] = CommitHook()
    repository: Optional[ProjectHook] = ProjectHook()
    project: Optional[ProjectHook] = ProjectHook()
    user_id: Optional[int] = 0
    user_name: Optional[str] = ""
    user: Optional[UserHook] = UserHook()
    pusher: Optional[UserHook] = UserHook()
    sender: Optional[UserHook] = UserHook()
    enterprise: Optional[EnterpriseHook] = EnterpriseHook()
    hook_name: Optional[str] = ""
    password: Optional[str] = ""


@dataclass
class TagPushEvent:
    action: Optional[str]
