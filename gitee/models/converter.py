import json
import dacite

from gitee.models.hook_event_types import *


def format_note_event(event: NoteEvent) -> NoteEvent:
    """
    Init NoteEvent to avoid errors when using nested class to get payload parameters
    """
    if not event.comment:
        event.comment = NoteEvent()
    if not event.repository:
        event.repository = ProjectHook()
    if not event.project:
        event.project = ProjectHook()
    if not event.author:
        event.author = UserHook()
    if not event.sender:
        event.sender = UserHook()
    if not event.enterprise:
        event.enterprise = EnterpriseHook()
    if not event.pull_request:
        event.pull_request = PullRequestHook()
    if not event.issue:
        event.issue = IssueHook()
    return event


def format_issue_event(event: IssueEvent) -> IssueEvent:
    """
    Init IssueEvent to avoid errors when using nested class to get payload parameters
    """
    if not event.issue:
        event.issue = IssueHook()
    if not event.repository:
        event.repository = ProjectHook()
    if not event.project:
        event.project = ProjectHook()
    if not event.sender:
        event.sender = UserHook()
    if not event.target_user:
        event.target_user = UserHook()
    if not event.user:
        event.user = UserHook()
    if not event.assignee:
        event.assignee = UserHook()
    if not event.updated_by:
        event.updated_by = UserHook()
    if not event.enterprise:
        event.enterprise = EnterpriseHook()
    return event


def format_pr_event(event: PullRequestEvent) -> PullRequestEvent:
    """
    Init PullRequestEvent to avoid errors when using nested class to get payload parameters
    """
    if not event.pull_request:
        event.pull_request = PullRequestHook()
    if not event.source_repo:
        event.source_repo = RepoInfo()
    if not event.target_repo:
        event.target_repo = RepoInfo()
    if not event.project:
        event.project = ProjectHook()
    if not event.repository:
        event.repository = ProjectHook()
    if not event.author:
        event.author = UserHook()
    if not event.updated_by:
        event.updated_by = UserHook()
    if not event.sender:
        event.sender = UserHook()
    if not event.target_user:
        event.target_user = UserHook()
    if not event.enterprise:
        event.enterprise = EnterpriseHook()
    return event


def format_push_event(event: PushEvent) -> PushEvent:
    """
    Init PushEvent to avoid errors when using nested class to get payload parameters
    """
    if not event.commits:
        event.commits = []
    if not event.head_commit:
        event.head_commit = CommitHook()
    if not event.repository:
        event.repository = ProjectHook()
    if not event.project:
        event.project = ProjectHook()
    if not event.user:
        event.user = UserHook()
    if not event.pusher:
        event.pusher = UserHook()
    if not event.sender:
        event.sender = UserHook()
    if not event.enterprise:
        event.enterprise = EnterpriseHook()
    return event


def convert_to_note_event(payload: str) -> NoteEvent:
    payload = json.loads(payload)
    event = dacite.from_dict(NoteEvent, payload)
    return format_note_event(event)


def convert_to_issue_event(payload: str) -> IssueEvent:
    payload = json.loads(payload)
    event = dacite.from_dict(IssueEvent, payload)
    return format_issue_event(event)


def convert_to_pr_event(payload: str) -> PullRequestEvent:
    payload = json.loads(payload)
    event = dacite.from_dict(PullRequestEvent, payload)
    return format_pr_event(event)


def convert_to_push_event(payload: str) -> PushEvent:
    payload = json.loads(payload)
    event = dacite.from_dict(PushEvent, payload)
    return format_push_event(event)
