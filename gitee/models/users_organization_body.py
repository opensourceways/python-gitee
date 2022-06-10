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

class UsersOrganizationBody(object):
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
        'name': 'str',
        'org': 'str',
        'description': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'name': 'name',
        'org': 'org',
        'description': 'description'
    }

    def __init__(self, access_token=None, name=None, org=None, description=None):  # noqa: E501
        """UsersOrganizationBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._name = None
        self._org = None
        self._description = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.name = name
        self.org = org
        if description is not None:
            self.description = description

    @property
    def access_token(self):
        """Gets the access_token of this UsersOrganizationBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this UsersOrganizationBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this UsersOrganizationBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this UsersOrganizationBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def name(self):
        """Gets the name of this UsersOrganizationBody.  # noqa: E501

        组织名称  # noqa: E501

        :return: The name of this UsersOrganizationBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UsersOrganizationBody.

        组织名称  # noqa: E501

        :param name: The name of this UsersOrganizationBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org(self):
        """Gets the org of this UsersOrganizationBody.  # noqa: E501

        组织的路径(path/login)  # noqa: E501

        :return: The org of this UsersOrganizationBody.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this UsersOrganizationBody.

        组织的路径(path/login)  # noqa: E501

        :param org: The org of this UsersOrganizationBody.  # noqa: E501
        :type: str
        """
        if org is None:
            raise ValueError("Invalid value for `org`, must not be `None`")  # noqa: E501

        self._org = org

    @property
    def description(self):
        """Gets the description of this UsersOrganizationBody.  # noqa: E501

        组织描述  # noqa: E501

        :return: The description of this UsersOrganizationBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UsersOrganizationBody.

        组织描述  # noqa: E501

        :param description: The description of this UsersOrganizationBody.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(UsersOrganizationBody, dict):
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
        if not isinstance(other, UsersOrganizationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
