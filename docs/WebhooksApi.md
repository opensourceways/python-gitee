# gitee.WebhooksApi

All URIs are relative to *https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_repos_owner_repo_hooks_id**](WebhooksApi.md#delete_v5_repos_owner_repo_hooks_id) | **DELETE** /v5/repos/{owner}/{repo}/hooks/{id} | 删除一个仓库WebHook
[**get_v5_repos_owner_repo_hooks**](WebhooksApi.md#get_v5_repos_owner_repo_hooks) | **GET** /v5/repos/{owner}/{repo}/hooks | 列出仓库的WebHooks
[**get_v5_repos_owner_repo_hooks_id**](WebhooksApi.md#get_v5_repos_owner_repo_hooks_id) | **GET** /v5/repos/{owner}/{repo}/hooks/{id} | 获取仓库单个WebHook
[**patch_v5_repos_owner_repo_hooks_id**](WebhooksApi.md#patch_v5_repos_owner_repo_hooks_id) | **PATCH** /v5/repos/{owner}/{repo}/hooks/{id} | 更新一个仓库WebHook
[**post_v5_repos_owner_repo_hooks**](WebhooksApi.md#post_v5_repos_owner_repo_hooks) | **POST** /v5/repos/{owner}/{repo}/hooks | 创建一个仓库WebHook
[**post_v5_repos_owner_repo_hooks_id_tests**](WebhooksApi.md#post_v5_repos_owner_repo_hooks_id_tests) | **POST** /v5/repos/{owner}/{repo}/hooks/{id}/tests | 测试WebHook是否发送成功


# **delete_v5_repos_owner_repo_hooks_id**
> delete_v5_repos_owner_repo_hooks_id(owner, repo, id, access_token=access_token)

删除一个仓库WebHook

删除一个仓库WebHook

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除一个仓库WebHook
    api_instance.delete_v5_repos_owner_repo_hooks_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_v5_repos_owner_repo_hooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_hooks**
> list[Hook] get_v5_repos_owner_repo_hooks(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出仓库的WebHooks

列出仓库的WebHooks

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出仓库的WebHooks
    api_response = api_instance.get_v5_repos_owner_repo_hooks(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_v5_repos_owner_repo_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Hook]**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_hooks_id**
> Hook get_v5_repos_owner_repo_hooks_id(owner, repo, id, access_token=access_token)

获取仓库单个WebHook

获取仓库单个WebHook

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库单个WebHook
    api_response = api_instance.get_v5_repos_owner_repo_hooks_id(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_v5_repos_owner_repo_hooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_hooks_id**
> Hook patch_v5_repos_owner_repo_hooks_id(owner, repo, id, url, access_token=access_token, password=password, push_events=push_events, tag_push_events=tag_push_events, issues_events=issues_events, note_events=note_events, merge_requests_events=merge_requests_events)

更新一个仓库WebHook

更新一个仓库WebHook

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
url = 'url_example' # str | 远程HTTP URL
access_token = 'access_token_example' # str | 用户授权码 (optional)
password = 'password_example' # str | 请求URL时会带上该密码，防止URL被恶意请求 (optional)
push_events = true # bool | Push代码到仓库 (optional) (default to true)
tag_push_events = true # bool | 提交Tag到仓库 (optional)
issues_events = true # bool | 创建/关闭Issue (optional)
note_events = true # bool | 评论了Issue/代码等等 (optional)
merge_requests_events = true # bool | 合并请求和合并后 (optional)

try:
    # 更新一个仓库WebHook
    api_response = api_instance.patch_v5_repos_owner_repo_hooks_id(owner, repo, id, url, access_token=access_token, password=password, push_events=push_events, tag_push_events=tag_push_events, issues_events=issues_events, note_events=note_events, merge_requests_events=merge_requests_events)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->patch_v5_repos_owner_repo_hooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **url** | **str**| 远程HTTP URL | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **password** | **str**| 请求URL时会带上该密码，防止URL被恶意请求 | [optional] 
 **push_events** | **bool**| Push代码到仓库 | [optional] [default to true]
 **tag_push_events** | **bool**| 提交Tag到仓库 | [optional] 
 **issues_events** | **bool**| 创建/关闭Issue | [optional] 
 **note_events** | **bool**| 评论了Issue/代码等等 | [optional] 
 **merge_requests_events** | **bool**| 合并请求和合并后 | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_hooks**
> Hook post_v5_repos_owner_repo_hooks(owner, repo, url, access_token=access_token, password=password, push_events=push_events, tag_push_events=tag_push_events, issues_events=issues_events, note_events=note_events, merge_requests_events=merge_requests_events)

创建一个仓库WebHook

创建一个仓库WebHook

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
url = 'url_example' # str | 远程HTTP URL
access_token = 'access_token_example' # str | 用户授权码 (optional)
password = 'password_example' # str | 请求URL时会带上该密码，防止URL被恶意请求 (optional)
push_events = true # bool | Push代码到仓库 (optional) (default to true)
tag_push_events = true # bool | 提交Tag到仓库 (optional)
issues_events = true # bool | 创建/关闭Issue (optional)
note_events = true # bool | 评论了Issue/代码等等 (optional)
merge_requests_events = true # bool | 合并请求和合并后 (optional)

try:
    # 创建一个仓库WebHook
    api_response = api_instance.post_v5_repos_owner_repo_hooks(owner, repo, url, access_token=access_token, password=password, push_events=push_events, tag_push_events=tag_push_events, issues_events=issues_events, note_events=note_events, merge_requests_events=merge_requests_events)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->post_v5_repos_owner_repo_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **url** | **str**| 远程HTTP URL | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **password** | **str**| 请求URL时会带上该密码，防止URL被恶意请求 | [optional] 
 **push_events** | **bool**| Push代码到仓库 | [optional] [default to true]
 **tag_push_events** | **bool**| 提交Tag到仓库 | [optional] 
 **issues_events** | **bool**| 创建/关闭Issue | [optional] 
 **note_events** | **bool**| 评论了Issue/代码等等 | [optional] 
 **merge_requests_events** | **bool**| 合并请求和合并后 | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_hooks_id_tests**
> post_v5_repos_owner_repo_hooks_id_tests(owner, repo, id, access_token=access_token)

测试WebHook是否发送成功

测试WebHook是否发送成功

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 测试WebHook是否发送成功
    api_instance.post_v5_repos_owner_repo_hooks_id_tests(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling WebhooksApi->post_v5_repos_owner_repo_hooks_id_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

