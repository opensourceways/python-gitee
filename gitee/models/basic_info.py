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


class BasicInfo(object):
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
        'label': 'str',
        'ref': 'str',
        'sha': 'str',
        'user': 'UserBasic',
        'repo': 'Project'
    }

    attribute_map = {
        'label': 'label',
        'ref': 'ref',
        'sha': 'sha',
        'user': 'user',
        'repo': 'repo'
    }

    def __init__(self, label=None, ref=None, sha=None, user=None, repo=None, _configuration=None):  # noqa: E501
        """BasicInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._label = None
        self._ref = None
        self._sha = None
        self._user = None
        self._repo = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if ref is not None:
            self.ref = ref
        if sha is not None:
            self.sha = sha
        if user is not None:
            self.user = user
        if repo is not None:
            self.repo = repo

    @property
    def label(self):
        """Gets the label of this BasicInfo.  # noqa: E501


        :return: The label of this BasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this BasicInfo.


        :param label: The label of this BasicInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def ref(self):
        """Gets the ref of this BasicInfo.  # noqa: E501


        :return: The ref of this BasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this BasicInfo.


        :param ref: The ref of this BasicInfo.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def sha(self):
        """Gets the sha of this BasicInfo.  # noqa: E501


        :return: The sha of this BasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this BasicInfo.


        :param sha: The sha of this BasicInfo.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def user(self):
        """Gets the user of this BasicInfo.  # noqa: E501


        :return: The user of this BasicInfo.  # noqa: E501
        :rtype: UserBasic
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BasicInfo.


        :param user: The user of this BasicInfo.  # noqa: E501
        :type: UserBasic
        """

        self._user = user

    @property
    def repo(self):
        """Gets the repo of this BasicInfo.  # noqa: E501


        :return: The repo of this BasicInfo.  # noqa: E501
        :rtype: Project
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this BasicInfo.


        :param repo: The repo of this BasicInfo.  # noqa: E501
        :type: Project
        """

        self._repo = repo

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
        if issubclass(BasicInfo, dict):
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
        if not isinstance(other, BasicInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicInfo):
            return True

        return self.to_dict() != other.to_dict()
