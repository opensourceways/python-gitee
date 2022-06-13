import json

import dacite

from gitee.models.converter import convert_to_push_event, convert_to_note_event
from gitee.models.hook_event_types import PushEvent


class Dog:
    type = 'animals'

    def __init__(self,name):
        self.name = name


if __name__ == '__main__':
    data = {'ref': 'ref', 'before': 'before', 'after': 'after', 'total_commits_count': 10,
            'commits_more_than_ten': False, 'created': True, 'deleted': False, 'compare': 'compare', 'commits': [],
            'head_commit': None, 'repository': None, 'project': None, 'user_id': 1, 'user_name': 'wwl', 'user': None,
            'pusher': None, 'sender': None, 'enterprise': None, 'hook_name': 'push', 'password': None}
    json_str = json.dumps(data)
    event = convert_to_push_event(json_str)
    print(event.enterprise.name)
