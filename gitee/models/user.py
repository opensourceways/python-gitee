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


class User(object):
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
        'blog': 'str',
        'weibo': 'str',
        'bio': 'str',
        'public_repos': 'str',
        'public_gists': 'str',
        'followers': 'str',
        'following': 'str',
        'stared': 'str',
        'watched': 'str',
        'created_at': 'str',
        'updated_at': 'str',
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
        'blog': 'blog',
        'weibo': 'weibo',
        'bio': 'bio',
        'public_repos': 'public_repos',
        'public_gists': 'public_gists',
        'followers': 'followers',
        'following': 'following',
        'stared': 'stared',
        'watched': 'watched',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'email': 'email'
    }

    def __init__(self, id=None, login=None, name=None, avatar_url=None, url=None, html_url=None, followers_url=None, following_url=None, gists_url=None, starred_url=None, subscriptions_url=None, organizations_url=None, repos_url=None, events_url=None, received_events_url=None, type=None, site_admin=None, blog=None, weibo=None, bio=None, public_repos=None, public_gists=None, followers=None, following=None, stared=None, watched=None, created_at=None, updated_at=None, email=None, _configuration=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
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
        self._blog = None
        self._weibo = None
        self._bio = None
        self._public_repos = None
        self._public_gists = None
        self._followers = None
        self._following = None
        self._stared = None
        self._watched = None
        self._created_at = None
        self._updated_at = None
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
        if blog is not None:
            self.blog = blog
        if weibo is not None:
            self.weibo = weibo
        if bio is not None:
            self.bio = bio
        if public_repos is not None:
            self.public_repos = public_repos
        if public_gists is not None:
            self.public_gists = public_gists
        if followers is not None:
            self.followers = followers
        if following is not None:
            self.following = following
        if stared is not None:
            self.stared = stared
        if watched is not None:
            self.watched = watched
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this User.  # noqa: E501


        :return: The login of this User.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this User.


        :param login: The login of this User.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this User.  # noqa: E501


        :return: The avatar_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this User.


        :param avatar_url: The avatar_url of this User.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def url(self):
        """Gets the url of this User.  # noqa: E501


        :return: The url of this User.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this User.


        :param url: The url of this User.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def html_url(self):
        """Gets the html_url of this User.  # noqa: E501


        :return: The html_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this User.


        :param html_url: The html_url of this User.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def followers_url(self):
        """Gets the followers_url of this User.  # noqa: E501


        :return: The followers_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._followers_url

    @followers_url.setter
    def followers_url(self, followers_url):
        """Sets the followers_url of this User.


        :param followers_url: The followers_url of this User.  # noqa: E501
        :type: str
        """

        self._followers_url = followers_url

    @property
    def following_url(self):
        """Gets the following_url of this User.  # noqa: E501


        :return: The following_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._following_url

    @following_url.setter
    def following_url(self, following_url):
        """Sets the following_url of this User.


        :param following_url: The following_url of this User.  # noqa: E501
        :type: str
        """

        self._following_url = following_url

    @property
    def gists_url(self):
        """Gets the gists_url of this User.  # noqa: E501


        :return: The gists_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._gists_url

    @gists_url.setter
    def gists_url(self, gists_url):
        """Sets the gists_url of this User.


        :param gists_url: The gists_url of this User.  # noqa: E501
        :type: str
        """

        self._gists_url = gists_url

    @property
    def starred_url(self):
        """Gets the starred_url of this User.  # noqa: E501


        :return: The starred_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._starred_url

    @starred_url.setter
    def starred_url(self, starred_url):
        """Sets the starred_url of this User.


        :param starred_url: The starred_url of this User.  # noqa: E501
        :type: str
        """

        self._starred_url = starred_url

    @property
    def subscriptions_url(self):
        """Gets the subscriptions_url of this User.  # noqa: E501


        :return: The subscriptions_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._subscriptions_url

    @subscriptions_url.setter
    def subscriptions_url(self, subscriptions_url):
        """Sets the subscriptions_url of this User.


        :param subscriptions_url: The subscriptions_url of this User.  # noqa: E501
        :type: str
        """

        self._subscriptions_url = subscriptions_url

    @property
    def organizations_url(self):
        """Gets the organizations_url of this User.  # noqa: E501


        :return: The organizations_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._organizations_url

    @organizations_url.setter
    def organizations_url(self, organizations_url):
        """Sets the organizations_url of this User.


        :param organizations_url: The organizations_url of this User.  # noqa: E501
        :type: str
        """

        self._organizations_url = organizations_url

    @property
    def repos_url(self):
        """Gets the repos_url of this User.  # noqa: E501


        :return: The repos_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._repos_url

    @repos_url.setter
    def repos_url(self, repos_url):
        """Sets the repos_url of this User.


        :param repos_url: The repos_url of this User.  # noqa: E501
        :type: str
        """

        self._repos_url = repos_url

    @property
    def events_url(self):
        """Gets the events_url of this User.  # noqa: E501


        :return: The events_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._events_url

    @events_url.setter
    def events_url(self, events_url):
        """Sets the events_url of this User.


        :param events_url: The events_url of this User.  # noqa: E501
        :type: str
        """

        self._events_url = events_url

    @property
    def received_events_url(self):
        """Gets the received_events_url of this User.  # noqa: E501


        :return: The received_events_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._received_events_url

    @received_events_url.setter
    def received_events_url(self, received_events_url):
        """Sets the received_events_url of this User.


        :param received_events_url: The received_events_url of this User.  # noqa: E501
        :type: str
        """

        self._received_events_url = received_events_url

    @property
    def type(self):
        """Gets the type of this User.  # noqa: E501


        :return: The type of this User.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this User.


        :param type: The type of this User.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def site_admin(self):
        """Gets the site_admin of this User.  # noqa: E501


        :return: The site_admin of this User.  # noqa: E501
        :rtype: bool
        """
        return self._site_admin

    @site_admin.setter
    def site_admin(self, site_admin):
        """Sets the site_admin of this User.


        :param site_admin: The site_admin of this User.  # noqa: E501
        :type: bool
        """

        self._site_admin = site_admin

    @property
    def blog(self):
        """Gets the blog of this User.  # noqa: E501


        :return: The blog of this User.  # noqa: E501
        :rtype: str
        """
        return self._blog

    @blog.setter
    def blog(self, blog):
        """Sets the blog of this User.


        :param blog: The blog of this User.  # noqa: E501
        :type: str
        """

        self._blog = blog

    @property
    def weibo(self):
        """Gets the weibo of this User.  # noqa: E501


        :return: The weibo of this User.  # noqa: E501
        :rtype: str
        """
        return self._weibo

    @weibo.setter
    def weibo(self, weibo):
        """Sets the weibo of this User.


        :param weibo: The weibo of this User.  # noqa: E501
        :type: str
        """

        self._weibo = weibo

    @property
    def bio(self):
        """Gets the bio of this User.  # noqa: E501


        :return: The bio of this User.  # noqa: E501
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this User.


        :param bio: The bio of this User.  # noqa: E501
        :type: str
        """

        self._bio = bio

    @property
    def public_repos(self):
        """Gets the public_repos of this User.  # noqa: E501


        :return: The public_repos of this User.  # noqa: E501
        :rtype: str
        """
        return self._public_repos

    @public_repos.setter
    def public_repos(self, public_repos):
        """Sets the public_repos of this User.


        :param public_repos: The public_repos of this User.  # noqa: E501
        :type: str
        """

        self._public_repos = public_repos

    @property
    def public_gists(self):
        """Gets the public_gists of this User.  # noqa: E501


        :return: The public_gists of this User.  # noqa: E501
        :rtype: str
        """
        return self._public_gists

    @public_gists.setter
    def public_gists(self, public_gists):
        """Sets the public_gists of this User.


        :param public_gists: The public_gists of this User.  # noqa: E501
        :type: str
        """

        self._public_gists = public_gists

    @property
    def followers(self):
        """Gets the followers of this User.  # noqa: E501


        :return: The followers of this User.  # noqa: E501
        :rtype: str
        """
        return self._followers

    @followers.setter
    def followers(self, followers):
        """Sets the followers of this User.


        :param followers: The followers of this User.  # noqa: E501
        :type: str
        """

        self._followers = followers

    @property
    def following(self):
        """Gets the following of this User.  # noqa: E501


        :return: The following of this User.  # noqa: E501
        :rtype: str
        """
        return self._following

    @following.setter
    def following(self, following):
        """Sets the following of this User.


        :param following: The following of this User.  # noqa: E501
        :type: str
        """

        self._following = following

    @property
    def stared(self):
        """Gets the stared of this User.  # noqa: E501


        :return: The stared of this User.  # noqa: E501
        :rtype: str
        """
        return self._stared

    @stared.setter
    def stared(self, stared):
        """Sets the stared of this User.


        :param stared: The stared of this User.  # noqa: E501
        :type: str
        """

        self._stared = stared

    @property
    def watched(self):
        """Gets the watched of this User.  # noqa: E501


        :return: The watched of this User.  # noqa: E501
        :rtype: str
        """
        return self._watched

    @watched.setter
    def watched(self, watched):
        """Sets the watched of this User.


        :param watched: The watched of this User.  # noqa: E501
        :type: str
        """

        self._watched = watched

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501


        :return: The created_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.


        :param created_at: The created_at of this User.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this User.  # noqa: E501


        :return: The updated_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this User.


        :param updated_at: The updated_at of this User.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
