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


class Code(object):
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
        'forks_url': 'str',
        'commits_url': 'str',
        'id': 'str',
        'description': 'str',
        'public': 'str',
        'owner': 'str',
        'user': 'str',
        'files': 'str',
        'truncated': 'str',
        'html_url': 'str',
        'comments': 'str',
        'comments_url': 'str',
        'git_pull_url': 'str',
        'git_push_url': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'url': 'url',
        'forks_url': 'forks_url',
        'commits_url': 'commits_url',
        'id': 'id',
        'description': 'description',
        'public': 'public',
        'owner': 'owner',
        'user': 'user',
        'files': 'files',
        'truncated': 'truncated',
        'html_url': 'html_url',
        'comments': 'comments',
        'comments_url': 'comments_url',
        'git_pull_url': 'git_pull_url',
        'git_push_url': 'git_push_url',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, url=None, forks_url=None, commits_url=None, id=None, description=None, public=None, owner=None, user=None, files=None, truncated=None, html_url=None, comments=None, comments_url=None, git_pull_url=None, git_push_url=None, created_at=None, updated_at=None):  # noqa: E501
        """Code - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._forks_url = None
        self._commits_url = None
        self._id = None
        self._description = None
        self._public = None
        self._owner = None
        self._user = None
        self._files = None
        self._truncated = None
        self._html_url = None
        self._comments = None
        self._comments_url = None
        self._git_pull_url = None
        self._git_push_url = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if forks_url is not None:
            self.forks_url = forks_url
        if commits_url is not None:
            self.commits_url = commits_url
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if public is not None:
            self.public = public
        if owner is not None:
            self.owner = owner
        if user is not None:
            self.user = user
        if files is not None:
            self.files = files
        if truncated is not None:
            self.truncated = truncated
        if html_url is not None:
            self.html_url = html_url
        if comments is not None:
            self.comments = comments
        if comments_url is not None:
            self.comments_url = comments_url
        if git_pull_url is not None:
            self.git_pull_url = git_pull_url
        if git_push_url is not None:
            self.git_push_url = git_push_url
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this Code.  # noqa: E501


        :return: The url of this Code.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Code.


        :param url: The url of this Code.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def forks_url(self):
        """Gets the forks_url of this Code.  # noqa: E501


        :return: The forks_url of this Code.  # noqa: E501
        :rtype: str
        """
        return self._forks_url

    @forks_url.setter
    def forks_url(self, forks_url):
        """Sets the forks_url of this Code.


        :param forks_url: The forks_url of this Code.  # noqa: E501
        :type: str
        """

        self._forks_url = forks_url

    @property
    def commits_url(self):
        """Gets the commits_url of this Code.  # noqa: E501


        :return: The commits_url of this Code.  # noqa: E501
        :rtype: str
        """
        return self._commits_url

    @commits_url.setter
    def commits_url(self, commits_url):
        """Sets the commits_url of this Code.


        :param commits_url: The commits_url of this Code.  # noqa: E501
        :type: str
        """

        self._commits_url = commits_url

    @property
    def id(self):
        """Gets the id of this Code.  # noqa: E501


        :return: The id of this Code.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Code.


        :param id: The id of this Code.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this Code.  # noqa: E501


        :return: The description of this Code.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Code.


        :param description: The description of this Code.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def public(self):
        """Gets the public of this Code.  # noqa: E501


        :return: The public of this Code.  # noqa: E501
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this Code.


        :param public: The public of this Code.  # noqa: E501
        :type: str
        """

        self._public = public

    @property
    def owner(self):
        """Gets the owner of this Code.  # noqa: E501


        :return: The owner of this Code.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Code.


        :param owner: The owner of this Code.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def user(self):
        """Gets the user of this Code.  # noqa: E501


        :return: The user of this Code.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Code.


        :param user: The user of this Code.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def files(self):
        """Gets the files of this Code.  # noqa: E501


        :return: The files of this Code.  # noqa: E501
        :rtype: str
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Code.


        :param files: The files of this Code.  # noqa: E501
        :type: str
        """

        self._files = files

    @property
    def truncated(self):
        """Gets the truncated of this Code.  # noqa: E501


        :return: The truncated of this Code.  # noqa: E501
        :rtype: str
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        """Sets the truncated of this Code.


        :param truncated: The truncated of this Code.  # noqa: E501
        :type: str
        """

        self._truncated = truncated

    @property
    def html_url(self):
        """Gets the html_url of this Code.  # noqa: E501


        :return: The html_url of this Code.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this Code.


        :param html_url: The html_url of this Code.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def comments(self):
        """Gets the comments of this Code.  # noqa: E501


        :return: The comments of this Code.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Code.


        :param comments: The comments of this Code.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def comments_url(self):
        """Gets the comments_url of this Code.  # noqa: E501


        :return: The comments_url of this Code.  # noqa: E501
        :rtype: str
        """
        return self._comments_url

    @comments_url.setter
    def comments_url(self, comments_url):
        """Sets the comments_url of this Code.


        :param comments_url: The comments_url of this Code.  # noqa: E501
        :type: str
        """

        self._comments_url = comments_url

    @property
    def git_pull_url(self):
        """Gets the git_pull_url of this Code.  # noqa: E501


        :return: The git_pull_url of this Code.  # noqa: E501
        :rtype: str
        """
        return self._git_pull_url

    @git_pull_url.setter
    def git_pull_url(self, git_pull_url):
        """Sets the git_pull_url of this Code.


        :param git_pull_url: The git_pull_url of this Code.  # noqa: E501
        :type: str
        """

        self._git_pull_url = git_pull_url

    @property
    def git_push_url(self):
        """Gets the git_push_url of this Code.  # noqa: E501


        :return: The git_push_url of this Code.  # noqa: E501
        :rtype: str
        """
        return self._git_push_url

    @git_push_url.setter
    def git_push_url(self, git_push_url):
        """Sets the git_push_url of this Code.


        :param git_push_url: The git_push_url of this Code.  # noqa: E501
        :type: str
        """

        self._git_push_url = git_push_url

    @property
    def created_at(self):
        """Gets the created_at of this Code.  # noqa: E501


        :return: The created_at of this Code.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Code.


        :param created_at: The created_at of this Code.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Code.  # noqa: E501


        :return: The updated_at of this Code.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Code.


        :param updated_at: The updated_at of this Code.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(Code, dict):
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
        if not isinstance(other, Code):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
