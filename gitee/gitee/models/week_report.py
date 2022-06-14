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


class WeekReport(object):
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
        'content': 'str',
        'content_html': 'str',
        'year': 'str',
        'month': 'str',
        'week_index': 'str',
        'week_begin': 'str',
        'week_end': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'user': 'UserMini'
    }

    attribute_map = {
        'id': 'id',
        'content': 'content',
        'content_html': 'content_html',
        'year': 'year',
        'month': 'month',
        'week_index': 'week_index',
        'week_begin': 'week_begin',
        'week_end': 'week_end',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, id=None, content=None, content_html=None, year=None, month=None, week_index=None, week_begin=None, week_end=None, created_at=None, updated_at=None, user=None, _configuration=None):  # noqa: E501
        """WeekReport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._content = None
        self._content_html = None
        self._year = None
        self._month = None
        self._week_index = None
        self._week_begin = None
        self._week_end = None
        self._created_at = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if content is not None:
            self.content = content
        if content_html is not None:
            self.content_html = content_html
        if year is not None:
            self.year = year
        if month is not None:
            self.month = month
        if week_index is not None:
            self.week_index = week_index
        if week_begin is not None:
            self.week_begin = week_begin
        if week_end is not None:
            self.week_end = week_end
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def id(self):
        """Gets the id of this WeekReport.  # noqa: E501


        :return: The id of this WeekReport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WeekReport.


        :param id: The id of this WeekReport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def content(self):
        """Gets the content of this WeekReport.  # noqa: E501


        :return: The content of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this WeekReport.


        :param content: The content of this WeekReport.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_html(self):
        """Gets the content_html of this WeekReport.  # noqa: E501


        :return: The content_html of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._content_html

    @content_html.setter
    def content_html(self, content_html):
        """Sets the content_html of this WeekReport.


        :param content_html: The content_html of this WeekReport.  # noqa: E501
        :type: str
        """

        self._content_html = content_html

    @property
    def year(self):
        """Gets the year of this WeekReport.  # noqa: E501


        :return: The year of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this WeekReport.


        :param year: The year of this WeekReport.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def month(self):
        """Gets the month of this WeekReport.  # noqa: E501


        :return: The month of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this WeekReport.


        :param month: The month of this WeekReport.  # noqa: E501
        :type: str
        """

        self._month = month

    @property
    def week_index(self):
        """Gets the week_index of this WeekReport.  # noqa: E501


        :return: The week_index of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._week_index

    @week_index.setter
    def week_index(self, week_index):
        """Sets the week_index of this WeekReport.


        :param week_index: The week_index of this WeekReport.  # noqa: E501
        :type: str
        """

        self._week_index = week_index

    @property
    def week_begin(self):
        """Gets the week_begin of this WeekReport.  # noqa: E501


        :return: The week_begin of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._week_begin

    @week_begin.setter
    def week_begin(self, week_begin):
        """Sets the week_begin of this WeekReport.


        :param week_begin: The week_begin of this WeekReport.  # noqa: E501
        :type: str
        """

        self._week_begin = week_begin

    @property
    def week_end(self):
        """Gets the week_end of this WeekReport.  # noqa: E501


        :return: The week_end of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._week_end

    @week_end.setter
    def week_end(self, week_end):
        """Sets the week_end of this WeekReport.


        :param week_end: The week_end of this WeekReport.  # noqa: E501
        :type: str
        """

        self._week_end = week_end

    @property
    def created_at(self):
        """Gets the created_at of this WeekReport.  # noqa: E501


        :return: The created_at of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WeekReport.


        :param created_at: The created_at of this WeekReport.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this WeekReport.  # noqa: E501


        :return: The updated_at of this WeekReport.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this WeekReport.


        :param updated_at: The updated_at of this WeekReport.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this WeekReport.  # noqa: E501


        :return: The user of this WeekReport.  # noqa: E501
        :rtype: UserMini
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WeekReport.


        :param user: The user of this WeekReport.  # noqa: E501
        :type: UserMini
        """

        self._user = user

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
        if issubclass(WeekReport, dict):
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
        if not isinstance(other, WeekReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WeekReport):
            return True

        return self.to_dict() != other.to_dict()
