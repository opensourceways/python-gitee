from dataclasses import dataclass, field
from typing import List, Optional

from gitee.models.model_issue import Issue


@dataclass
class LabelHook:
    id: Optional[int]
    name: Optional[str]
    color: Optional[str]


@dataclass
class UserHook:
    id: Optional[int] = 0
    name: Optional[str] = ""
    email: Optional[str] = ""
    user_name: Optional[str] = ""
    url: Optional[str] = ""
    login: Optional[str] = ""
    avatar_url: Optional[str] = ""
    html_url: Optional[str] = ""
    type: Optional[str] = ""
    site_admin: Optional[str] = ""
    time: Optional[str] = ""
    remark: Optional[str] = ""


# EnterpriseHook : 企业信息
@dataclass
class EnterpriseHook:
    name: Optional[str] = ""
    url: Optional[str] = ""


# NoteHook : 评论信息
@dataclass
class NoteHook:
    id: Optional[int] = 0
    body: Optional[str] = ""
    user: Optional[UserHook] = UserHook()
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""
    html_url: Optional[str] = ""
    position: Optional[str] = ""
    commit_id: Optional[str] = ""


# ProjectHook : project 信息
@dataclass
class ProjectHook:
    id: Optional[int] = 0
    name: Optional[str] = ""
    path: Optional[str] = ""
    full_name: Optional[str] = ""
    owner: Optional[UserHook] = UserHook()
    private: Optional[bool] = False
    html_url: Optional[str] = ""
    url: Optional[str] = ""
    description: Optional[str] = ""
    fork: Optional[bool] = False
    pushed_at: Optional[str] = ""
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""
    ssh_url: Optional[str] = ""
    git_url: Optional[str] = ""
    clone_url: Optional[str] = ""
    svn_url: Optional[str] = ""
    git_http_url: Optional[str] = ""
    git_ssh_url: Optional[str] = ""
    git_svn_url: Optional[str] = ""
    homepage: Optional[str] = ""
    stargazers_count: Optional[int] = 0
    watchers_count: Optional[int] = 0
    forks_count: Optional[int] = 0
    language: Optional[str] = ""

    has_issues: Optional[bool] = False
    has_wiki: Optional[bool] = False
    has_pages: Optional[bool] = False
    license: Optional[str] = ""

    open_issues_count: Optional[int] = 0
    default_branch: Optional[str] = ""
    namespace: Optional[str] = ""

    name_with_namespace: Optional[str] = ""
    path_with_namespace: Optional[str] = ""


# MilestoneHook : 里程碑信息
@dataclass
class MilestoneHook:
    id: Optional[int] = 0
    html_url: Optional[str] = ""
    number: Optional[int] = 0
    title: Optional[str] = ""
    description: Optional[str] = ""
    open_issues: Optional[int] = 0
    closed_issues: Optional[int] = 0
    state: Optional[str] = ""
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""
    due_on: Optional[str] = ""


# BranchHook : 分支信息
@dataclass
class BranchHook:
    label: Optional[str] = ""
    ref: Optional[str] = ""
    sha: Optional[str] = ""
    user: Optional[UserHook] = UserHook()
    repo: Optional[ProjectHook] = ProjectHook()


# PullRequestHook : PR 信息
@dataclass
class PullRequestHook:
    id: Optional[int] = 0
    number: Optional[int] = 0
    state: Optional[str] = ""
    html_url: Optional[str] = ""
    diff_url: Optional[str] = ""
    patch_url: Optional[str] = ""
    title: Optional[str] = ""
    body: Optional[str] = ""
    stale_labels: Optional[List[LabelHook]] = field(default_factory=list)
    labels: Optional[List[LabelHook]] = field(default_factory=list)
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""
    closed_at: Optional[str] = ""
    merged_at: Optional[str] = ""
    merge_commit_sha: Optional[str] = ""
    merge_reference_name: Optional[str] = ""
    user: Optional[UserHook] = UserHook()
    assignee: Optional[UserHook] = UserHook()
    assignees: Optional[List[UserHook]] = field(default_factory=list)
    tester: Optional[List[UserHook]] = field(default_factory=list)
    testers: Optional[List[UserHook]] = field(default_factory=list)
    need_test: Optional[bool] = False
    need_review: Optional[bool] = False
    milestone: Optional[MilestoneHook] = MilestoneHook()
    head: Optional[BranchHook] = BranchHook()
    base: Optional[BranchHook] = BranchHook()
    merged: Optional[bool] = False
    mergeable: Optional[bool] = False
    merge_status: Optional[str] = ""
    updated_by: Optional[UserHook] = UserHook()
    comments: Optional[int] = 0
    commits: Optional[int] = 0
    additions: Optional[int] = 0
    deletions: Optional[int] = 0
    changed_files: Optional[int] = 0
    issues: Optional[List[Issue]] = field(default_factory=list)
    stale_issues: Optional[List[Issue]] = field(default_factory=list)


# IssueHook : issue 信息
@dataclass
class IssueHook:
    id: Optional[int] = 0
    html_url: Optional[str] = ""
    number: Optional[str] = ""
    title: Optional[str] = ""
    user: Optional[UserHook] = UserHook()
    labels: Optional[List[LabelHook]] = field(default_factory=list)
    state: Optional[str] = ""
    state_name: Optional[str] = ""
    type_name: Optional[str] = ""
    assignee: Optional[UserHook] = UserHook()
    collaborators: Optional[List[UserHook]] = field(default_factory=list)
    milestone: Optional[MilestoneHook] = MilestoneHook()
    comments: Optional[int] = 0
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""
    body: Optional[str] = ""


# CommitHook : git commit 中的信息
@dataclass
class CommitHook:
    id: Optional[str] = ""
    tree_id: Optional[str] = ""
    parent_ids: Optional[List[str]] = field(default_factory=list)
    message: Optional[str] = ""
    timestamp: Optional[str] = ""
    url: Optional[str] = ""
    author: Optional[UserHook] = UserHook()
    committer: Optional[UserHook] = UserHook()
    distinct: Optional[bool] = False
    added: Optional[List[str]] = field(default_factory=list)
    removed: Optional[List[str]] = field(default_factory=list)
    modified: Optional[List[str]] = field(default_factory=list)
