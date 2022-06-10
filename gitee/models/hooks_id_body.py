# coding: utf-8

"""
    码云 Open API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HooksIdBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token': 'str',
        'url': 'str',
        'password': 'str',
        'push_events': 'bool',
        'tag_push_events': 'bool',
        'issues_events': 'bool',
        'note_events': 'bool',
        'merge_requests_events': 'bool'
    }

    attribute_map = {
        'access_token': 'access_token',
        'url': 'url',
        'password': 'password',
        'push_events': 'push_events',
        'tag_push_events': 'tag_push_events',
        'issues_events': 'issues_events',
        'note_events': 'note_events',
        'merge_requests_events': 'merge_requests_events'
    }

    def __init__(self, access_token=None, url=None, password=None, push_events=True, tag_push_events=None, issues_events=None, note_events=None, merge_requests_events=None):  # noqa: E501
        """HooksIdBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._url = None
        self._password = None
        self._push_events = None
        self._tag_push_events = None
        self._issues_events = None
        self._note_events = None
        self._merge_requests_events = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.url = url
        if password is not None:
            self.password = password
        if push_events is not None:
            self.push_events = push_events
        if tag_push_events is not None:
            self.tag_push_events = tag_push_events
        if issues_events is not None:
            self.issues_events = issues_events
        if note_events is not None:
            self.note_events = note_events
        if merge_requests_events is not None:
            self.merge_requests_events = merge_requests_events

    @property
    def access_token(self):
        """Gets the access_token of this HooksIdBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this HooksIdBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this HooksIdBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this HooksIdBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def url(self):
        """Gets the url of this HooksIdBody.  # noqa: E501

        远程HTTP URL  # noqa: E501

        :return: The url of this HooksIdBody.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HooksIdBody.

        远程HTTP URL  # noqa: E501

        :param url: The url of this HooksIdBody.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def password(self):
        """Gets the password of this HooksIdBody.  # noqa: E501

        请求URL时会带上该密码，防止URL被恶意请求  # noqa: E501

        :return: The password of this HooksIdBody.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this HooksIdBody.

        请求URL时会带上该密码，防止URL被恶意请求  # noqa: E501

        :param password: The password of this HooksIdBody.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def push_events(self):
        """Gets the push_events of this HooksIdBody.  # noqa: E501

        Push代码到仓库  # noqa: E501

        :return: The push_events of this HooksIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._push_events

    @push_events.setter
    def push_events(self, push_events):
        """Sets the push_events of this HooksIdBody.

        Push代码到仓库  # noqa: E501

        :param push_events: The push_events of this HooksIdBody.  # noqa: E501
        :type: bool
        """

        self._push_events = push_events

    @property
    def tag_push_events(self):
        """Gets the tag_push_events of this HooksIdBody.  # noqa: E501

        提交Tag到仓库  # noqa: E501

        :return: The tag_push_events of this HooksIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._tag_push_events

    @tag_push_events.setter
    def tag_push_events(self, tag_push_events):
        """Sets the tag_push_events of this HooksIdBody.

        提交Tag到仓库  # noqa: E501

        :param tag_push_events: The tag_push_events of this HooksIdBody.  # noqa: E501
        :type: bool
        """

        self._tag_push_events = tag_push_events

    @property
    def issues_events(self):
        """Gets the issues_events of this HooksIdBody.  # noqa: E501

        创建/关闭Issue  # noqa: E501

        :return: The issues_events of this HooksIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._issues_events

    @issues_events.setter
    def issues_events(self, issues_events):
        """Sets the issues_events of this HooksIdBody.

        创建/关闭Issue  # noqa: E501

        :param issues_events: The issues_events of this HooksIdBody.  # noqa: E501
        :type: bool
        """

        self._issues_events = issues_events

    @property
    def note_events(self):
        """Gets the note_events of this HooksIdBody.  # noqa: E501

        评论了Issue/代码等等  # noqa: E501

        :return: The note_events of this HooksIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._note_events

    @note_events.setter
    def note_events(self, note_events):
        """Sets the note_events of this HooksIdBody.

        评论了Issue/代码等等  # noqa: E501

        :param note_events: The note_events of this HooksIdBody.  # noqa: E501
        :type: bool
        """

        self._note_events = note_events

    @property
    def merge_requests_events(self):
        """Gets the merge_requests_events of this HooksIdBody.  # noqa: E501

        合并请求和合并后  # noqa: E501

        :return: The merge_requests_events of this HooksIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._merge_requests_events

    @merge_requests_events.setter
    def merge_requests_events(self, merge_requests_events):
        """Sets the merge_requests_events of this HooksIdBody.

        合并请求和合并后  # noqa: E501

        :param merge_requests_events: The merge_requests_events of this HooksIdBody.  # noqa: E501
        :type: bool
        """

        self._merge_requests_events = merge_requests_events

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(HooksIdBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HooksIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
