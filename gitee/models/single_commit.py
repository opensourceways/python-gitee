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


class SingleCommit(object):
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
        'author': 'GitUser',
        'committer': 'GitUser',
        'tree': 'CommitTree'
    }

    attribute_map = {
        'author': 'author',
        'committer': 'committer',
        'tree': 'tree'
    }

    def __init__(self, author=None, committer=None, tree=None, _configuration=None):  # noqa: E501
        """SingleCommit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._author = None
        self._committer = None
        self._tree = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if committer is not None:
            self.committer = committer
        if tree is not None:
            self.tree = tree

    @property
    def author(self):
        """Gets the author of this SingleCommit.  # noqa: E501


        :return: The author of this SingleCommit.  # noqa: E501
        :rtype: GitUser
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this SingleCommit.


        :param author: The author of this SingleCommit.  # noqa: E501
        :type: GitUser
        """

        self._author = author

    @property
    def committer(self):
        """Gets the committer of this SingleCommit.  # noqa: E501


        :return: The committer of this SingleCommit.  # noqa: E501
        :rtype: GitUser
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """Sets the committer of this SingleCommit.


        :param committer: The committer of this SingleCommit.  # noqa: E501
        :type: GitUser
        """

        self._committer = committer

    @property
    def tree(self):
        """Gets the tree of this SingleCommit.  # noqa: E501


        :return: The tree of this SingleCommit.  # noqa: E501
        :rtype: CommitTree
        """
        return self._tree

    @tree.setter
    def tree(self, tree):
        """Sets the tree of this SingleCommit.


        :param tree: The tree of this SingleCommit.  # noqa: E501
        :type: CommitTree
        """

        self._tree = tree

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
        if issubclass(SingleCommit, dict):
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
        if not isinstance(other, SingleCommit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SingleCommit):
            return True

        return self.to_dict() != other.to_dict()
