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


class MilestonesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_v5_repos_owner_repo_milestones_number(self, owner, repo, number, **kwargs):  # noqa: E501
        """删除仓库单个里程碑  # noqa: E501

        删除仓库单个里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_v5_repos_owner_repo_milestones_number(owner, repo, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int number: 里程碑序号(id) (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, **kwargs)  # noqa: E501
            return data

    def delete_v5_repos_owner_repo_milestones_number_with_http_info(self, owner, repo, number, **kwargs):  # noqa: E501
        """删除仓库单个里程碑  # noqa: E501

        删除仓库单个里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int number: 里程碑序号(id) (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'number', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_v5_repos_owner_repo_milestones_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in params or
                                                       params['owner'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `owner` when calling `delete_v5_repos_owner_repo_milestones_number`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `delete_v5_repos_owner_repo_milestones_number`")  # noqa: E501
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in params or
                                                       params['number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `number` when calling `delete_v5_repos_owner_repo_milestones_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

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
            '/v5/repos/{owner}/{repo}/milestones/{number}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v5_repos_owner_repo_milestones(self, owner, repo, **kwargs):  # noqa: E501
        """获取仓库所有里程碑  # noqa: E501

        获取仓库所有里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_repos_owner_repo_milestones(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :param str state: 里程碑状态: open, closed, all。默认: open
        :param str sort: 排序方式: due_on
        :param str direction: 升序(asc)或是降序(desc)。默认: asc
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :return: list[Milestone]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v5_repos_owner_repo_milestones_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v5_repos_owner_repo_milestones_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def get_v5_repos_owner_repo_milestones_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """获取仓库所有里程碑  # noqa: E501

        获取仓库所有里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_repos_owner_repo_milestones_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :param str state: 里程碑状态: open, closed, all。默认: open
        :param str sort: 排序方式: due_on
        :param str direction: 升序(asc)或是降序(desc)。默认: asc
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :return: list[Milestone]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'access_token', 'state', 'sort', 'direction', 'page', 'per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v5_repos_owner_repo_milestones" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in params or
                                                       params['owner'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `owner` when calling `get_v5_repos_owner_repo_milestones`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `get_v5_repos_owner_repo_milestones`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'direction' in params:
            query_params.append(('direction', params['direction']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

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
            '/v5/repos/{owner}/{repo}/milestones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Milestone]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v5_repos_owner_repo_milestones_number(self, owner, repo, number, **kwargs):  # noqa: E501
        """获取仓库单个里程碑  # noqa: E501

        获取仓库单个里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_repos_owner_repo_milestones_number(owner, repo, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int number: 里程碑序号(id) (required)
        :param str access_token: 用户授权码
        :return: Milestone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, **kwargs)  # noqa: E501
            return data

    def get_v5_repos_owner_repo_milestones_number_with_http_info(self, owner, repo, number, **kwargs):  # noqa: E501
        """获取仓库单个里程碑  # noqa: E501

        获取仓库单个里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int number: 里程碑序号(id) (required)
        :param str access_token: 用户授权码
        :return: Milestone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'number', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v5_repos_owner_repo_milestones_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in params or
                                                       params['owner'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `owner` when calling `get_v5_repos_owner_repo_milestones_number`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `get_v5_repos_owner_repo_milestones_number`")  # noqa: E501
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in params or
                                                       params['number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `number` when calling `get_v5_repos_owner_repo_milestones_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

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
            '/v5/repos/{owner}/{repo}/milestones/{number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Milestone',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_v5_repos_owner_repo_milestones_number(self, owner, repo, number, title, due_on, **kwargs):  # noqa: E501
        """更新仓库里程碑  # noqa: E501

        更新仓库里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_v5_repos_owner_repo_milestones_number(owner, repo, number, title, due_on, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int number: 里程碑序号(id) (required)
        :param str title: 里程碑标题 (required)
        :param str due_on: 里程碑的截止日期 (required)
        :param str access_token: 用户授权码
        :param str state: 里程碑状态: open, closed, all。默认: open
        :param str description: 里程碑具体描述
        :return: Milestone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, title, due_on, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, title, due_on, **kwargs)  # noqa: E501
            return data

    def patch_v5_repos_owner_repo_milestones_number_with_http_info(self, owner, repo, number, title, due_on, **kwargs):  # noqa: E501
        """更新仓库里程碑  # noqa: E501

        更新仓库里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_v5_repos_owner_repo_milestones_number_with_http_info(owner, repo, number, title, due_on, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int number: 里程碑序号(id) (required)
        :param str title: 里程碑标题 (required)
        :param str due_on: 里程碑的截止日期 (required)
        :param str access_token: 用户授权码
        :param str state: 里程碑状态: open, closed, all。默认: open
        :param str description: 里程碑具体描述
        :return: Milestone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'number', 'title', 'due_on', 'access_token', 'state', 'description']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_v5_repos_owner_repo_milestones_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in params or
                                                       params['owner'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `owner` when calling `patch_v5_repos_owner_repo_milestones_number`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `patch_v5_repos_owner_repo_milestones_number`")  # noqa: E501
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in params or
                                                       params['number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `number` when calling `patch_v5_repos_owner_repo_milestones_number`")  # noqa: E501
        # verify the required parameter 'title' is set
        if self.api_client.client_side_validation and ('title' not in params or
                                                       params['title'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `title` when calling `patch_v5_repos_owner_repo_milestones_number`")  # noqa: E501
        # verify the required parameter 'due_on' is set
        if self.api_client.client_side_validation and ('due_on' not in params or
                                                       params['due_on'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `due_on` when calling `patch_v5_repos_owner_repo_milestones_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'access_token' in params:
            form_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'title' in params:
            form_params.append(('title', params['title']))  # noqa: E501
        if 'state' in params:
            form_params.append(('state', params['state']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'due_on' in params:
            form_params.append(('due_on', params['due_on']))  # noqa: E501

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
            '/v5/repos/{owner}/{repo}/milestones/{number}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Milestone',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_v5_repos_owner_repo_milestones(self, owner, repo, title, due_on, **kwargs):  # noqa: E501
        """创建仓库里程碑  # noqa: E501

        创建仓库里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v5_repos_owner_repo_milestones(owner, repo, title, due_on, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str title: 里程碑标题 (required)
        :param str due_on: 里程碑的截止日期 (required)
        :param str access_token: 用户授权码
        :param str state: 里程碑状态: open, closed, all。默认: open
        :param str description: 里程碑具体描述
        :return: Milestone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_v5_repos_owner_repo_milestones_with_http_info(owner, repo, title, due_on, **kwargs)  # noqa: E501
        else:
            (data) = self.post_v5_repos_owner_repo_milestones_with_http_info(owner, repo, title, due_on, **kwargs)  # noqa: E501
            return data

    def post_v5_repos_owner_repo_milestones_with_http_info(self, owner, repo, title, due_on, **kwargs):  # noqa: E501
        """创建仓库里程碑  # noqa: E501

        创建仓库里程碑  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v5_repos_owner_repo_milestones_with_http_info(owner, repo, title, due_on, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str title: 里程碑标题 (required)
        :param str due_on: 里程碑的截止日期 (required)
        :param str access_token: 用户授权码
        :param str state: 里程碑状态: open, closed, all。默认: open
        :param str description: 里程碑具体描述
        :return: Milestone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'title', 'due_on', 'access_token', 'state', 'description']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_v5_repos_owner_repo_milestones" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in params or
                                                       params['owner'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `owner` when calling `post_v5_repos_owner_repo_milestones`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `post_v5_repos_owner_repo_milestones`")  # noqa: E501
        # verify the required parameter 'title' is set
        if self.api_client.client_side_validation and ('title' not in params or
                                                       params['title'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `title` when calling `post_v5_repos_owner_repo_milestones`")  # noqa: E501
        # verify the required parameter 'due_on' is set
        if self.api_client.client_side_validation and ('due_on' not in params or
                                                       params['due_on'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `due_on` when calling `post_v5_repos_owner_repo_milestones`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'access_token' in params:
            form_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'title' in params:
            form_params.append(('title', params['title']))  # noqa: E501
        if 'state' in params:
            form_params.append(('state', params['state']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'due_on' in params:
            form_params.append(('due_on', params['due_on']))  # noqa: E501

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
            '/v5/repos/{owner}/{repo}/milestones', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Milestone',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
