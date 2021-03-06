# coding: utf-8

"""
    码云 Open API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import gitee
from gitee.api.webhooks_api import WebhooksApi  # noqa: E501
from gitee.rest import ApiException


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    def setUp(self):
        self.api = gitee.api.webhooks_api.WebhooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_v5_repos_owner_repo_hooks_id(self):
        """Test case for delete_v5_repos_owner_repo_hooks_id

        删除一个仓库WebHook  # noqa: E501
        """
        pass

    def test_get_v5_repos_owner_repo_hooks(self):
        """Test case for get_v5_repos_owner_repo_hooks

        列出仓库的WebHooks  # noqa: E501
        """
        pass

    def test_get_v5_repos_owner_repo_hooks_id(self):
        """Test case for get_v5_repos_owner_repo_hooks_id

        获取仓库单个WebHook  # noqa: E501
        """
        pass

    def test_patch_v5_repos_owner_repo_hooks_id(self):
        """Test case for patch_v5_repos_owner_repo_hooks_id

        更新一个仓库WebHook  # noqa: E501
        """
        pass

    def test_post_v5_repos_owner_repo_hooks(self):
        """Test case for post_v5_repos_owner_repo_hooks

        创建一个仓库WebHook  # noqa: E501
        """
        pass

    def test_post_v5_repos_owner_repo_hooks_id_tests(self):
        """Test case for post_v5_repos_owner_repo_hooks_id_tests

        测试WebHook是否发送成功  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
