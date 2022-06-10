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

class PullRequestComments(object):
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
        'url': 'str',
        'id': 'int',
        'path': 'str',
        'position': 'str',
        'original_position': 'str',
        'commit_id': 'str',
        'original_commit_id': 'str',
        'user': 'UserBasic',
        'body': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'html_url': 'str',
        'pull_request_url': 'str',
        'links': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'path': 'path',
        'position': 'position',
        'original_position': 'original_position',
        'commit_id': 'commit_id',
        'original_commit_id': 'original_commit_id',
        'user': 'user',
        'body': 'body',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'html_url': 'html_url',
        'pull_request_url': 'pull_request_url',
        'links': '_links'
    }

    def __init__(self, url=None, id=None, path=None, position=None, original_position=None, commit_id=None, original_commit_id=None, user=None, body=None, created_at=None, updated_at=None, html_url=None, pull_request_url=None, links=None):  # noqa: E501
        """PullRequestComments - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._id = None
        self._path = None
        self._position = None
        self._original_position = None
        self._commit_id = None
        self._original_commit_id = None
        self._user = None
        self._body = None
        self._created_at = None
        self._updated_at = None
        self._html_url = None
        self._pull_request_url = None
        self._links = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if position is not None:
            self.position = position
        if original_position is not None:
            self.original_position = original_position
        if commit_id is not None:
            self.commit_id = commit_id
        if original_commit_id is not None:
            self.original_commit_id = original_commit_id
        if user is not None:
            self.user = user
        if body is not None:
            self.body = body
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if html_url is not None:
            self.html_url = html_url
        if pull_request_url is not None:
            self.pull_request_url = pull_request_url
        if links is not None:
            self.links = links

    @property
    def url(self):
        """Gets the url of this PullRequestComments.  # noqa: E501


        :return: The url of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PullRequestComments.


        :param url: The url of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this PullRequestComments.  # noqa: E501


        :return: The id of this PullRequestComments.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PullRequestComments.


        :param id: The id of this PullRequestComments.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this PullRequestComments.  # noqa: E501


        :return: The path of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PullRequestComments.


        :param path: The path of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def position(self):
        """Gets the position of this PullRequestComments.  # noqa: E501


        :return: The position of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PullRequestComments.


        :param position: The position of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def original_position(self):
        """Gets the original_position of this PullRequestComments.  # noqa: E501


        :return: The original_position of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._original_position

    @original_position.setter
    def original_position(self, original_position):
        """Sets the original_position of this PullRequestComments.


        :param original_position: The original_position of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._original_position = original_position

    @property
    def commit_id(self):
        """Gets the commit_id of this PullRequestComments.  # noqa: E501


        :return: The commit_id of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this PullRequestComments.


        :param commit_id: The commit_id of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def original_commit_id(self):
        """Gets the original_commit_id of this PullRequestComments.  # noqa: E501


        :return: The original_commit_id of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._original_commit_id

    @original_commit_id.setter
    def original_commit_id(self, original_commit_id):
        """Sets the original_commit_id of this PullRequestComments.


        :param original_commit_id: The original_commit_id of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._original_commit_id = original_commit_id

    @property
    def user(self):
        """Gets the user of this PullRequestComments.  # noqa: E501


        :return: The user of this PullRequestComments.  # noqa: E501
        :rtype: UserBasic
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PullRequestComments.


        :param user: The user of this PullRequestComments.  # noqa: E501
        :type: UserBasic
        """

        self._user = user

    @property
    def body(self):
        """Gets the body of this PullRequestComments.  # noqa: E501


        :return: The body of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PullRequestComments.


        :param body: The body of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def created_at(self):
        """Gets the created_at of this PullRequestComments.  # noqa: E501


        :return: The created_at of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PullRequestComments.


        :param created_at: The created_at of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PullRequestComments.  # noqa: E501


        :return: The updated_at of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PullRequestComments.


        :param updated_at: The updated_at of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def html_url(self):
        """Gets the html_url of this PullRequestComments.  # noqa: E501


        :return: The html_url of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this PullRequestComments.


        :param html_url: The html_url of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def pull_request_url(self):
        """Gets the pull_request_url of this PullRequestComments.  # noqa: E501


        :return: The pull_request_url of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._pull_request_url

    @pull_request_url.setter
    def pull_request_url(self, pull_request_url):
        """Sets the pull_request_url of this PullRequestComments.


        :param pull_request_url: The pull_request_url of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._pull_request_url = pull_request_url

    @property
    def links(self):
        """Gets the links of this PullRequestComments.  # noqa: E501


        :return: The links of this PullRequestComments.  # noqa: E501
        :rtype: str
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PullRequestComments.


        :param links: The links of this PullRequestComments.  # noqa: E501
        :type: str
        """

        self._links = links

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
        if issubclass(PullRequestComments, dict):
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
        if not isinstance(other, PullRequestComments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other