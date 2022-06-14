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


class PullRequestFilePath(object):
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
        'diff': 'str',
        'new_path': 'str',
        'old_path': 'str',
        'a_mode': 'str',
        'b_mode': 'str',
        'new_file': 'bool',
        'renamed_file': 'bool',
        'deleted_file': 'bool',
        'too_large': 'bool'
    }

    attribute_map = {
        'diff': 'diff',
        'new_path': 'new_path',
        'old_path': 'old_path',
        'a_mode': 'a_mode',
        'b_mode': 'b_mode',
        'new_file': 'new_file',
        'renamed_file': 'renamed_file',
        'deleted_file': 'deleted_file',
        'too_large': 'too_large'
    }

    def __init__(self, diff=None, new_path=None, old_path=None, a_mode=None, b_mode=None, new_file=None, renamed_file=None, deleted_file=None, too_large=None, _configuration=None):  # noqa: E501
        """PullRequestFilePath - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._diff = None
        self._new_path = None
        self._old_path = None
        self._a_mode = None
        self._b_mode = None
        self._new_file = None
        self._renamed_file = None
        self._deleted_file = None
        self._too_large = None
        self.discriminator = None

        if diff is not None:
            self.diff = diff
        if new_path is not None:
            self.new_path = new_path
        if old_path is not None:
            self.old_path = old_path
        if a_mode is not None:
            self.a_mode = a_mode
        if b_mode is not None:
            self.b_mode = b_mode
        if new_file is not None:
            self.new_file = new_file
        if renamed_file is not None:
            self.renamed_file = renamed_file
        if deleted_file is not None:
            self.deleted_file = deleted_file
        if too_large is not None:
            self.too_large = too_large

    @property
    def diff(self):
        """Gets the diff of this PullRequestFilePath.  # noqa: E501


        :return: The diff of this PullRequestFilePath.  # noqa: E501
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this PullRequestFilePath.


        :param diff: The diff of this PullRequestFilePath.  # noqa: E501
        :type: str
        """

        self._diff = diff

    @property
    def new_path(self):
        """Gets the new_path of this PullRequestFilePath.  # noqa: E501


        :return: The new_path of this PullRequestFilePath.  # noqa: E501
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        """Sets the new_path of this PullRequestFilePath.


        :param new_path: The new_path of this PullRequestFilePath.  # noqa: E501
        :type: str
        """

        self._new_path = new_path

    @property
    def old_path(self):
        """Gets the old_path of this PullRequestFilePath.  # noqa: E501


        :return: The old_path of this PullRequestFilePath.  # noqa: E501
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        """Sets the old_path of this PullRequestFilePath.


        :param old_path: The old_path of this PullRequestFilePath.  # noqa: E501
        :type: str
        """

        self._old_path = old_path

    @property
    def a_mode(self):
        """Gets the a_mode of this PullRequestFilePath.  # noqa: E501


        :return: The a_mode of this PullRequestFilePath.  # noqa: E501
        :rtype: str
        """
        return self._a_mode

    @a_mode.setter
    def a_mode(self, a_mode):
        """Sets the a_mode of this PullRequestFilePath.


        :param a_mode: The a_mode of this PullRequestFilePath.  # noqa: E501
        :type: str
        """

        self._a_mode = a_mode

    @property
    def b_mode(self):
        """Gets the b_mode of this PullRequestFilePath.  # noqa: E501


        :return: The b_mode of this PullRequestFilePath.  # noqa: E501
        :rtype: str
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        """Sets the b_mode of this PullRequestFilePath.


        :param b_mode: The b_mode of this PullRequestFilePath.  # noqa: E501
        :type: str
        """

        self._b_mode = b_mode

    @property
    def new_file(self):
        """Gets the new_file of this PullRequestFilePath.  # noqa: E501


        :return: The new_file of this PullRequestFilePath.  # noqa: E501
        :rtype: bool
        """
        return self._new_file

    @new_file.setter
    def new_file(self, new_file):
        """Sets the new_file of this PullRequestFilePath.


        :param new_file: The new_file of this PullRequestFilePath.  # noqa: E501
        :type: bool
        """

        self._new_file = new_file

    @property
    def renamed_file(self):
        """Gets the renamed_file of this PullRequestFilePath.  # noqa: E501


        :return: The renamed_file of this PullRequestFilePath.  # noqa: E501
        :rtype: bool
        """
        return self._renamed_file

    @renamed_file.setter
    def renamed_file(self, renamed_file):
        """Sets the renamed_file of this PullRequestFilePath.


        :param renamed_file: The renamed_file of this PullRequestFilePath.  # noqa: E501
        :type: bool
        """

        self._renamed_file = renamed_file

    @property
    def deleted_file(self):
        """Gets the deleted_file of this PullRequestFilePath.  # noqa: E501


        :return: The deleted_file of this PullRequestFilePath.  # noqa: E501
        :rtype: bool
        """
        return self._deleted_file

    @deleted_file.setter
    def deleted_file(self, deleted_file):
        """Sets the deleted_file of this PullRequestFilePath.


        :param deleted_file: The deleted_file of this PullRequestFilePath.  # noqa: E501
        :type: bool
        """

        self._deleted_file = deleted_file

    @property
    def too_large(self):
        """Gets the too_large of this PullRequestFilePath.  # noqa: E501


        :return: The too_large of this PullRequestFilePath.  # noqa: E501
        :rtype: bool
        """
        return self._too_large

    @too_large.setter
    def too_large(self, too_large):
        """Sets the too_large of this PullRequestFilePath.


        :param too_large: The too_large of this PullRequestFilePath.  # noqa: E501
        :type: bool
        """

        self._too_large = too_large

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
        if issubclass(PullRequestFilePath, dict):
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
        if not isinstance(other, PullRequestFilePath):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PullRequestFilePath):
            return True

        return self.to_dict() != other.to_dict()
