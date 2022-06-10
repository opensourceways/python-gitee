# coding: utf-8

"""
    码云 Open API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gitee.api_client import ApiClient


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_v5_search_gists(self, q, **kwargs):  # noqa: E501
        """搜索代码片段  # noqa: E501

        搜索代码片段  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_search_gists(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str language: 筛选指定语言的代码片段
        :param str owner: 筛选所属用户 (username/login) 的代码片段
        :param str sort: 排序字段，created_at(创建时间)、updated_at(更新时间)、notes_count(评论数)、stars_count(收藏数)、forks_count(Fork 数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: list[Code]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v5_search_gists_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v5_search_gists_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def get_v5_search_gists_with_http_info(self, q, **kwargs):  # noqa: E501
        """搜索代码片段  # noqa: E501

        搜索代码片段  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_search_gists_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str language: 筛选指定语言的代码片段
        :param str owner: 筛选所属用户 (username/login) 的代码片段
        :param str sort: 排序字段，created_at(创建时间)、updated_at(更新时间)、notes_count(评论数)、stars_count(收藏数)、forks_count(Fork 数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: list[Code]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'access_token', 'page', 'per_page', 'language', 'owner', 'sort', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v5_search_gists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `get_v5_search_gists`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/search/gists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Code]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v5_search_issues(self, q, **kwargs):  # noqa: E501
        """搜索 Issues  # noqa: E501

        搜索 Issues  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_search_issues(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str repo: 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues
        :param str language: 筛选指定语言的 issues
        :param str label: 筛选指定标签的 issues
        :param str state: 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝)
        :param str author: 筛选指定创建者 (username/login) 的 issues
        :param str assignee: 筛选指定负责人 (username/login) 的 issues
        :param str sort: 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: list[Issue]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v5_search_issues_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v5_search_issues_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def get_v5_search_issues_with_http_info(self, q, **kwargs):  # noqa: E501
        """搜索 Issues  # noqa: E501

        搜索 Issues  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_search_issues_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str repo: 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues
        :param str language: 筛选指定语言的 issues
        :param str label: 筛选指定标签的 issues
        :param str state: 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝)
        :param str author: 筛选指定创建者 (username/login) 的 issues
        :param str assignee: 筛选指定负责人 (username/login) 的 issues
        :param str sort: 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: list[Issue]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'access_token', 'page', 'per_page', 'repo', 'language', 'label', 'state', 'author', 'assignee', 'sort', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v5_search_issues" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `get_v5_search_issues`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'repo' in params:
            query_params.append(('repo', params['repo']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'label' in params:
            query_params.append(('label', params['label']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'author' in params:
            query_params.append(('author', params['author']))  # noqa: E501
        if 'assignee' in params:
            query_params.append(('assignee', params['assignee']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/search/issues', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Issue]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v5_search_repositories(self, q, **kwargs):  # noqa: E501
        """搜索仓库  # noqa: E501

        搜索仓库  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_search_repositories(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str owner: 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库
        :param bool fork: 是否搜索含 fork 的仓库，默认：否
        :param str language: 筛选指定语言的仓库
        :param str sort: 排序字段，created_at(创建时间)、last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: list[Project]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v5_search_repositories_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v5_search_repositories_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def get_v5_search_repositories_with_http_info(self, q, **kwargs):  # noqa: E501
        """搜索仓库  # noqa: E501

        搜索仓库  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_search_repositories_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str owner: 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库
        :param bool fork: 是否搜索含 fork 的仓库，默认：否
        :param str language: 筛选指定语言的仓库
        :param str sort: 排序字段，created_at(创建时间)、last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: list[Project]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'access_token', 'page', 'per_page', 'owner', 'fork', 'language', 'sort', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v5_search_repositories" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `get_v5_search_repositories`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501
        if 'fork' in params:
            query_params.append(('fork', params['fork']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/search/repositories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Project]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v5_search_users(self, q, **kwargs):  # noqa: E501
        """搜索用户  # noqa: E501

        搜索用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_search_users(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str sort: 排序字段，joined_at(注册时间)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v5_search_users_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v5_search_users_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def get_v5_search_users_with_http_info(self, q, **kwargs):  # noqa: E501
        """搜索用户  # noqa: E501

        搜索用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_search_users_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str sort: 排序字段，joined_at(注册时间)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'access_token', 'page', 'per_page', 'sort', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v5_search_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `get_v5_search_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/search/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[User]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
