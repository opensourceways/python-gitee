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
from gitee.api.emails_api import EmailsApi  # noqa: E501
from gitee.rest import ApiException


class TestEmailsApi(unittest.TestCase):
    """EmailsApi unit test stubs"""

    def setUp(self):
        self.api = gitee.api.emails_api.EmailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_v5_emails(self):
        """Test case for get_v5_emails

        获取授权用户的所有邮箱  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
