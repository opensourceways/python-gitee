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

from gitee.configuration import Configuration


class ProjectBasic(object):
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
        'id': 'int',
        'full_name': 'str',
        'human_name': 'str',
        'url': 'str',
        'namespace': 'object',
        'path': 'str',
        'name': 'str',
        'owner': 'UserBasic',
        'description': 'str',
        'private': 'bool',
        'public': 'bool',
        'internal': 'bool',
        'fork': 'bool',
        'html_url': 'str',
        'ssh_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'full_name': 'full_name',
        'human_name': 'human_name',
        'url': 'url',
        'namespace': 'namespace',
        'path': 'path',
        'name': 'name',
        'owner': 'owner',
        'description': 'description',
        'private': 'private',
        'public': 'public',
        'internal': 'internal',
        'fork': 'fork',
        'html_url': 'html_url',
        'ssh_url': 'ssh_url'
    }

    def __init__(self, id=None, full_name=None, human_name=None, url=None, namespace=None, path=None, name=None, owner=None, description=None, private=None, public=None, internal=None, fork=None, html_url=None, ssh_url=None, _configuration=None):  # noqa: E501
        """ProjectBasic - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._full_name = None
        self._human_name = None
        self._url = None
        self._namespace = None
        self._path = None
        self._name = None
        self._owner = None
        self._description = None
        self._private = None
        self._public = None
        self._internal = None
        self._fork = None
        self._html_url = None
        self._ssh_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if full_name is not None:
            self.full_name = full_name
        if human_name is not None:
            self.human_name = human_name
        if url is not None:
            self.url = url
        if namespace is not None:
            self.namespace = namespace
        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if description is not None:
            self.description = description
        if private is not None:
            self.private = private
        if public is not None:
            self.public = public
        if internal is not None:
            self.internal = internal
        if fork is not None:
            self.fork = fork
        if html_url is not None:
            self.html_url = html_url
        if ssh_url is not None:
            self.ssh_url = ssh_url

    @property
    def id(self):
        """Gets the id of this ProjectBasic.  # noqa: E501


        :return: The id of this ProjectBasic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectBasic.


        :param id: The id of this ProjectBasic.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def full_name(self):
        """Gets the full_name of this ProjectBasic.  # noqa: E501


        :return: The full_name of this ProjectBasic.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ProjectBasic.


        :param full_name: The full_name of this ProjectBasic.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def human_name(self):
        """Gets the human_name of this ProjectBasic.  # noqa: E501


        :return: The human_name of this ProjectBasic.  # noqa: E501
        :rtype: str
        """
        return self._human_name

    @human_name.setter
    def human_name(self, human_name):
        """Sets the human_name of this ProjectBasic.


        :param human_name: The human_name of this ProjectBasic.  # noqa: E501
        :type: str
        """

        self._human_name = human_name

    @property
    def url(self):
        """Gets the url of this ProjectBasic.  # noqa: E501


        :return: The url of this ProjectBasic.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProjectBasic.


        :param url: The url of this ProjectBasic.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def namespace(self):
        """Gets the namespace of this ProjectBasic.  # noqa: E501


        :return: The namespace of this ProjectBasic.  # noqa: E501
        :rtype: object
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ProjectBasic.


        :param namespace: The namespace of this ProjectBasic.  # noqa: E501
        :type: object
        """

        self._namespace = namespace

    @property
    def path(self):
        """Gets the path of this ProjectBasic.  # noqa: E501


        :return: The path of this ProjectBasic.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ProjectBasic.


        :param path: The path of this ProjectBasic.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def name(self):
        """Gets the name of this ProjectBasic.  # noqa: E501


        :return: The name of this ProjectBasic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectBasic.


        :param name: The name of this ProjectBasic.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this ProjectBasic.  # noqa: E501


        :return: The owner of this ProjectBasic.  # noqa: E501
        :rtype: UserBasic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ProjectBasic.


        :param owner: The owner of this ProjectBasic.  # noqa: E501
        :type: UserBasic
        """

        self._owner = owner

    @property
    def description(self):
        """Gets the description of this ProjectBasic.  # noqa: E501


        :return: The description of this ProjectBasic.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectBasic.


        :param description: The description of this ProjectBasic.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def private(self):
        """Gets the private of this ProjectBasic.  # noqa: E501


        :return: The private of this ProjectBasic.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this ProjectBasic.


        :param private: The private of this ProjectBasic.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def public(self):
        """Gets the public of this ProjectBasic.  # noqa: E501


        :return: The public of this ProjectBasic.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ProjectBasic.


        :param public: The public of this ProjectBasic.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def internal(self):
        """Gets the internal of this ProjectBasic.  # noqa: E501


        :return: The internal of this ProjectBasic.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this ProjectBasic.


        :param internal: The internal of this ProjectBasic.  # noqa: E501
        :type: bool
        """

        self._internal = internal

    @property
    def fork(self):
        """Gets the fork of this ProjectBasic.  # noqa: E501


        :return: The fork of this ProjectBasic.  # noqa: E501
        :rtype: bool
        """
        return self._fork

    @fork.setter
    def fork(self, fork):
        """Sets the fork of this ProjectBasic.


        :param fork: The fork of this ProjectBasic.  # noqa: E501
        :type: bool
        """

        self._fork = fork

    @property
    def html_url(self):
        """Gets the html_url of this ProjectBasic.  # noqa: E501


        :return: The html_url of this ProjectBasic.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this ProjectBasic.


        :param html_url: The html_url of this ProjectBasic.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def ssh_url(self):
        """Gets the ssh_url of this ProjectBasic.  # noqa: E501


        :return: The ssh_url of this ProjectBasic.  # noqa: E501
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        """Sets the ssh_url of this ProjectBasic.


        :param ssh_url: The ssh_url of this ProjectBasic.  # noqa: E501
        :type: str
        """

        self._ssh_url = ssh_url

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
        if issubclass(ProjectBasic, dict):
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
        if not isinstance(other, ProjectBasic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectBasic):
            return True

        return self.to_dict() != other.to_dict()
