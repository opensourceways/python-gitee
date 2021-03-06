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


class SetRepoReviewer(object):
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
        'assignees': 'str',
        'testers': 'str',
        'assignees_number': 'int',
        'testers_number': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'assignees': 'assignees',
        'testers': 'testers',
        'assignees_number': 'assignees_number',
        'testers_number': 'testers_number'
    }

    def __init__(self, access_token=None, assignees=None, testers=None, assignees_number=None, testers_number=None, _configuration=None):  # noqa: E501
        """SetRepoReviewer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._assignees = None
        self._testers = None
        self._assignees_number = None
        self._testers_number = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if assignees is not None:
            self.assignees = assignees
        if testers is not None:
            self.testers = testers
        if assignees_number is not None:
            self.assignees_number = assignees_number
        if testers_number is not None:
            self.testers_number = testers_number

    @property
    def access_token(self):
        """Gets the access_token of this SetRepoReviewer.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this SetRepoReviewer.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this SetRepoReviewer.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this SetRepoReviewer.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def assignees(self):
        """Gets the assignees of this SetRepoReviewer.  # noqa: E501

        审查人员  # noqa: E501

        :return: The assignees of this SetRepoReviewer.  # noqa: E501
        :rtype: str
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        """Sets the assignees of this SetRepoReviewer.

        审查人员  # noqa: E501

        :param assignees: The assignees of this SetRepoReviewer.  # noqa: E501
        :type: str
        """

        self._assignees = assignees

    @property
    def testers(self):
        """Gets the testers of this SetRepoReviewer.  # noqa: E501

        测试人员  # noqa: E501

        :return: The testers of this SetRepoReviewer.  # noqa: E501
        :rtype: str
        """
        return self._testers

    @testers.setter
    def testers(self, testers):
        """Sets the testers of this SetRepoReviewer.

        测试人员  # noqa: E501

        :param testers: The testers of this SetRepoReviewer.  # noqa: E501
        :type: str
        """

        self._testers = testers

    @property
    def assignees_number(self):
        """Gets the assignees_number of this SetRepoReviewer.  # noqa: E501

        最少审查人数  # noqa: E501

        :return: The assignees_number of this SetRepoReviewer.  # noqa: E501
        :rtype: int
        """
        return self._assignees_number

    @assignees_number.setter
    def assignees_number(self, assignees_number):
        """Sets the assignees_number of this SetRepoReviewer.

        最少审查人数  # noqa: E501

        :param assignees_number: The assignees_number of this SetRepoReviewer.  # noqa: E501
        :type: int
        """

        self._assignees_number = assignees_number

    @property
    def testers_number(self):
        """Gets the testers_number of this SetRepoReviewer.  # noqa: E501

        最少测试人员  # noqa: E501

        :return: The testers_number of this SetRepoReviewer.  # noqa: E501
        :rtype: int
        """
        return self._testers_number

    @testers_number.setter
    def testers_number(self, testers_number):
        """Sets the testers_number of this SetRepoReviewer.

        最少测试人员  # noqa: E501

        :param testers_number: The testers_number of this SetRepoReviewer.  # noqa: E501
        :type: int
        """

        self._testers_number = testers_number

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
        if issubclass(SetRepoReviewer, dict):
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
        if not isinstance(other, SetRepoReviewer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetRepoReviewer):
            return True

        return self.to_dict() != other.to_dict()
