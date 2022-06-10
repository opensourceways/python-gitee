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


class Tag(object):
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
        'name': 'str',
        'commit': 'str'
    }

    attribute_map = {
        'name': 'name',
        'commit': 'commit'
    }

    def __init__(self, name=None, commit=None):  # noqa: E501
        """Tag - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._commit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if commit is not None:
            self.commit = commit

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501


        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.


        :param name: The name of this Tag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def commit(self):
        """Gets the commit of this Tag.  # noqa: E501


        :return: The commit of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this Tag.


        :param commit: The commit of this Tag.  # noqa: E501
        :type: str
        """

        self._commit = commit

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
        if issubclass(Tag, dict):
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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
