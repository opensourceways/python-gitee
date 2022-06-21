from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelUserBasic:
    id: Optional[int] = 0
    login: Optional[str] = ""
    name: Optional[str] = ""
    avatar_url: Optional[str] = ""
    url: Optional[str] = ""
    html_url: Optional[str] = ""
    followers_url: Optional[str] = ""
    following_url: Optional[str] = ""
    gists_url: Optional[str] = ""
    starred_url: Optional[str] = ""
    subscriptions_url: Optional[str] = ""
    organizations_url: Optional[str] = ""
    repos_url: Optional[str] = ""
    events_url: Optional[str] = ""
    received_events_url: Optional[str] = ""
    type: Optional[str] = ""
    site_admin: Optional[bool] = False
    email: Optional[str] = ""
