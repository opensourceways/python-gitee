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


class ProgramBasic(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'assignee': 'str',
        'author': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'assignee': 'assignee',
        'author': 'author'
    }

    def __init__(self, id=None, name=None, description=None, assignee=None, author=None, _configuration=None):  # noqa: E501
        """ProgramBasic - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._assignee = None
        self._author = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if assignee is not None:
            self.assignee = assignee
        if author is not None:
            self.author = author

    @property
    def id(self):
        """Gets the id of this ProgramBasic.  # noqa: E501


        :return: The id of this ProgramBasic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProgramBasic.


        :param id: The id of this ProgramBasic.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProgramBasic.  # noqa: E501


        :return: The name of this ProgramBasic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProgramBasic.


        :param name: The name of this ProgramBasic.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProgramBasic.  # noqa: E501


        :return: The description of this ProgramBasic.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProgramBasic.


        :param description: The description of this ProgramBasic.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def assignee(self):
        """Gets the assignee of this ProgramBasic.  # noqa: E501


        :return: The assignee of this ProgramBasic.  # noqa: E501
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this ProgramBasic.


        :param assignee: The assignee of this ProgramBasic.  # noqa: E501
        :type: str
        """

        self._assignee = assignee

    @property
    def author(self):
        """Gets the author of this ProgramBasic.  # noqa: E501


        :return: The author of this ProgramBasic.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ProgramBasic.


        :param author: The author of this ProgramBasic.  # noqa: E501
        :type: str
        """

        self._author = author

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
        if issubclass(ProgramBasic, dict):
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
        if not isinstance(other, ProgramBasic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProgramBasic):
            return True

        return self.to_dict() != other.to_dict()
