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


class UserBasic(object):
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
        'login': 'str',
        'name': 'str',
        'avatar_url': 'str',
        'url': 'str',
        'html_url': 'str',
        'followers_url': 'str',
        'following_url': 'str',
        'gists_url': 'str',
        'starred_url': 'str',
        'subscriptions_url': 'str',
        'organizations_url': 'str',
        'repos_url': 'str',
        'events_url': 'str',
        'received_events_url': 'str',
        'type': 'str',
        'site_admin': 'bool',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'login': 'login',
        'name': 'name',
        'avatar_url': 'avatar_url',
        'url': 'url',
        'html_url': 'html_url',
        'followers_url': 'followers_url',
        'following_url': 'following_url',
        'gists_url': 'gists_url',
        'starred_url': 'starred_url',
        'subscriptions_url': 'subscriptions_url',
        'organizations_url': 'organizations_url',
        'repos_url': 'repos_url',
        'events_url': 'events_url',
        'received_events_url': 'received_events_url',
        'type': 'type',
        'site_admin': 'site_admin',
        'email': 'email'
    }

    def __init__(self, id=None, login=None, name=None, avatar_url=None, url=None, html_url=None, followers_url=None, following_url=None, gists_url=None, starred_url=None, subscriptions_url=None, organizations_url=None, repos_url=None, events_url=None, received_events_url=None, type=None, site_admin=None, email=None, _configuration=None):  # noqa: E501
        """UserBasic - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._login = None
        self._name = None
        self._avatar_url = None
        self._url = None
        self._html_url = None
        self._followers_url = None
        self._following_url = None
        self._gists_url = None
        self._starred_url = None
        self._subscriptions_url = None
        self._organizations_url = None
        self._repos_url = None
        self._events_url = None
        self._received_events_url = None
        self._type = None
        self._site_admin = None
        self._email = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if name is not None:
            self.name = name
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if url is not None:
            self.url = url
        if html_url is not None:
            self.html_url = html_url
        if followers_url is not None:
            self.followers_url = followers_url
        if following_url is not None:
            self.following_url = following_url
        if gists_url is not None:
            self.gists_url = gists_url
        if starred_url is not None:
            self.starred_url = starred_url
        if subscriptions_url is not None:
            self.subscriptions_url = subscriptions_url
        if organizations_url is not None:
            self.organizations_url = organizations_url
        if repos_url is not None:
            self.repos_url = repos_url
        if events_url is not None:
            self.events_url = events_url
        if received_events_url is not None:
            self.received_events_url = received_events_url
        if type is not None:
            self.type = type
        if site_admin is not None:
            self.site_admin = site_admin
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this UserBasic.  # noqa: E501


        :return: The id of this UserBasic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserBasic.


        :param id: The id of this UserBasic.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this UserBasic.  # noqa: E501


        :return: The login of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UserBasic.


        :param login: The login of this UserBasic.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def name(self):
        """Gets the name of this UserBasic.  # noqa: E501


        :return: The name of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserBasic.


        :param name: The name of this UserBasic.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this UserBasic.  # noqa: E501


        :return: The avatar_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this UserBasic.


        :param avatar_url: The avatar_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def url(self):
        """Gets the url of this UserBasic.  # noqa: E501


        :return: The url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UserBasic.


        :param url: The url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def html_url(self):
        """Gets the html_url of this UserBasic.  # noqa: E501


        :return: The html_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this UserBasic.


        :param html_url: The html_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def followers_url(self):
        """Gets the followers_url of this UserBasic.  # noqa: E501


        :return: The followers_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._followers_url

    @followers_url.setter
    def followers_url(self, followers_url):
        """Sets the followers_url of this UserBasic.


        :param followers_url: The followers_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._followers_url = followers_url

    @property
    def following_url(self):
        """Gets the following_url of this UserBasic.  # noqa: E501


        :return: The following_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._following_url

    @following_url.setter
    def following_url(self, following_url):
        """Sets the following_url of this UserBasic.


        :param following_url: The following_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._following_url = following_url

    @property
    def gists_url(self):
        """Gets the gists_url of this UserBasic.  # noqa: E501


        :return: The gists_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._gists_url

    @gists_url.setter
    def gists_url(self, gists_url):
        """Sets the gists_url of this UserBasic.


        :param gists_url: The gists_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._gists_url = gists_url

    @property
    def starred_url(self):
        """Gets the starred_url of this UserBasic.  # noqa: E501


        :return: The starred_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._starred_url

    @starred_url.setter
    def starred_url(self, starred_url):
        """Sets the starred_url of this UserBasic.


        :param starred_url: The starred_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._starred_url = starred_url

    @property
    def subscriptions_url(self):
        """Gets the subscriptions_url of this UserBasic.  # noqa: E501


        :return: The subscriptions_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._subscriptions_url

    @subscriptions_url.setter
    def subscriptions_url(self, subscriptions_url):
        """Sets the subscriptions_url of this UserBasic.


        :param subscriptions_url: The subscriptions_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._subscriptions_url = subscriptions_url

    @property
    def organizations_url(self):
        """Gets the organizations_url of this UserBasic.  # noqa: E501


        :return: The organizations_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._organizations_url

    @organizations_url.setter
    def organizations_url(self, organizations_url):
        """Sets the organizations_url of this UserBasic.


        :param organizations_url: The organizations_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._organizations_url = organizations_url

    @property
    def repos_url(self):
        """Gets the repos_url of this UserBasic.  # noqa: E501


        :return: The repos_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._repos_url

    @repos_url.setter
    def repos_url(self, repos_url):
        """Sets the repos_url of this UserBasic.


        :param repos_url: The repos_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._repos_url = repos_url

    @property
    def events_url(self):
        """Gets the events_url of this UserBasic.  # noqa: E501


        :return: The events_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._events_url

    @events_url.setter
    def events_url(self, events_url):
        """Sets the events_url of this UserBasic.


        :param events_url: The events_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._events_url = events_url

    @property
    def received_events_url(self):
        """Gets the received_events_url of this UserBasic.  # noqa: E501


        :return: The received_events_url of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._received_events_url

    @received_events_url.setter
    def received_events_url(self, received_events_url):
        """Sets the received_events_url of this UserBasic.


        :param received_events_url: The received_events_url of this UserBasic.  # noqa: E501
        :type: str
        """

        self._received_events_url = received_events_url

    @property
    def type(self):
        """Gets the type of this UserBasic.  # noqa: E501


        :return: The type of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserBasic.


        :param type: The type of this UserBasic.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def site_admin(self):
        """Gets the site_admin of this UserBasic.  # noqa: E501


        :return: The site_admin of this UserBasic.  # noqa: E501
        :rtype: bool
        """
        return self._site_admin

    @site_admin.setter
    def site_admin(self, site_admin):
        """Sets the site_admin of this UserBasic.


        :param site_admin: The site_admin of this UserBasic.  # noqa: E501
        :type: bool
        """

        self._site_admin = site_admin

    @property
    def email(self):
        """Gets the email of this UserBasic.  # noqa: E501


        :return: The email of this UserBasic.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserBasic.


        :param email: The email of this UserBasic.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(UserBasic, dict):
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
        if not isinstance(other, UserBasic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserBasic):
            return True

        return self.to_dict() != other.to_dict()
