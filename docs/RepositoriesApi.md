# gitee.RepositoriesApi

All URIs are relative to *https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_repos_owner_repo**](RepositoriesApi.md#delete_v5_repos_owner_repo) | **DELETE** /v5/repos/{owner}/{repo} | 删除一个仓库
[**delete_v5_repos_owner_repo_branches_branch_protection**](RepositoriesApi.md#delete_v5_repos_owner_repo_branches_branch_protection) | **DELETE** /v5/repos/{owner}/{repo}/branches/{branch}/protection | 取消保护分支的设置
[**delete_v5_repos_owner_repo_collaborators_username**](RepositoriesApi.md#delete_v5_repos_owner_repo_collaborators_username) | **DELETE** /v5/repos/{owner}/{repo}/collaborators/{username} | 移除仓库成员
[**delete_v5_repos_owner_repo_comments_id**](RepositoriesApi.md#delete_v5_repos_owner_repo_comments_id) | **DELETE** /v5/repos/{owner}/{repo}/comments/{id} | 删除Commit评论
[**delete_v5_repos_owner_repo_contents_path**](RepositoriesApi.md#delete_v5_repos_owner_repo_contents_path) | **DELETE** /v5/repos/{owner}/{repo}/contents/{path} | 删除文件
[**delete_v5_repos_owner_repo_keys_enable_id**](RepositoriesApi.md#delete_v5_repos_owner_repo_keys_enable_id) | **DELETE** /v5/repos/{owner}/{repo}/keys/enable/{id} | 停用仓库公钥
[**delete_v5_repos_owner_repo_keys_id**](RepositoriesApi.md#delete_v5_repos_owner_repo_keys_id) | **DELETE** /v5/repos/{owner}/{repo}/keys/{id} | 删除一个仓库公钥
[**delete_v5_repos_owner_repo_releases_id**](RepositoriesApi.md#delete_v5_repos_owner_repo_releases_id) | **DELETE** /v5/repos/{owner}/{repo}/releases/{id} | 删除仓库Release
[**get_v5_enterprises_enterprise_repos**](RepositoriesApi.md#get_v5_enterprises_enterprise_repos) | **GET** /v5/enterprises/{enterprise}/repos | 获取企业的所有仓库
[**get_v5_orgs_org_repos**](RepositoriesApi.md#get_v5_orgs_org_repos) | **GET** /v5/orgs/{org}/repos | 获取一个组织的仓库
[**get_v5_repos_owner_repo**](RepositoriesApi.md#get_v5_repos_owner_repo) | **GET** /v5/repos/{owner}/{repo} | 获取用户的某个仓库
[**get_v5_repos_owner_repo_branches**](RepositoriesApi.md#get_v5_repos_owner_repo_branches) | **GET** /v5/repos/{owner}/{repo}/branches | 获取所有分支
[**get_v5_repos_owner_repo_branches_branch**](RepositoriesApi.md#get_v5_repos_owner_repo_branches_branch) | **GET** /v5/repos/{owner}/{repo}/branches/{branch} | 获取单个分支
[**get_v5_repos_owner_repo_collaborators**](RepositoriesApi.md#get_v5_repos_owner_repo_collaborators) | **GET** /v5/repos/{owner}/{repo}/collaborators | 获取仓库的所有成员
[**get_v5_repos_owner_repo_collaborators_username**](RepositoriesApi.md#get_v5_repos_owner_repo_collaborators_username) | **GET** /v5/repos/{owner}/{repo}/collaborators/{username} | 判断用户是否为仓库成员
[**get_v5_repos_owner_repo_collaborators_username_permission**](RepositoriesApi.md#get_v5_repos_owner_repo_collaborators_username_permission) | **GET** /v5/repos/{owner}/{repo}/collaborators/{username}/permission | 查看仓库成员的权限
[**get_v5_repos_owner_repo_comments**](RepositoriesApi.md#get_v5_repos_owner_repo_comments) | **GET** /v5/repos/{owner}/{repo}/comments | 获取仓库的Commit评论
[**get_v5_repos_owner_repo_comments_id**](RepositoriesApi.md#get_v5_repos_owner_repo_comments_id) | **GET** /v5/repos/{owner}/{repo}/comments/{id} | 获取仓库的某条Commit评论
[**get_v5_repos_owner_repo_commits**](RepositoriesApi.md#get_v5_repos_owner_repo_commits) | **GET** /v5/repos/{owner}/{repo}/commits | 仓库的所有提交
[**get_v5_repos_owner_repo_commits_ref_comments**](RepositoriesApi.md#get_v5_repos_owner_repo_commits_ref_comments) | **GET** /v5/repos/{owner}/{repo}/commits/{ref}/comments | 获取单个Commit的评论
[**get_v5_repos_owner_repo_commits_sha**](RepositoriesApi.md#get_v5_repos_owner_repo_commits_sha) | **GET** /v5/repos/{owner}/{repo}/commits/{sha} | 仓库的某个提交
[**get_v5_repos_owner_repo_compare_base___head**](RepositoriesApi.md#get_v5_repos_owner_repo_compare_base___head) | **GET** /v5/repos/{owner}/{repo}/compare/{base}...{head} | 两个Commits之间对比的版本差异
[**get_v5_repos_owner_repo_contents_path**](RepositoriesApi.md#get_v5_repos_owner_repo_contents_path) | **GET** /v5/repos/{owner}/{repo}/contents/{path} | 获取仓库具体路径下的内容
[**get_v5_repos_owner_repo_contributors**](RepositoriesApi.md#get_v5_repos_owner_repo_contributors) | **GET** /v5/repos/{owner}/{repo}/contributors | 获取仓库贡献者
[**get_v5_repos_owner_repo_forks**](RepositoriesApi.md#get_v5_repos_owner_repo_forks) | **GET** /v5/repos/{owner}/{repo}/forks | 查看仓库的Forks
[**get_v5_repos_owner_repo_keys**](RepositoriesApi.md#get_v5_repos_owner_repo_keys) | **GET** /v5/repos/{owner}/{repo}/keys | 获取仓库已部署的公钥
[**get_v5_repos_owner_repo_keys_available**](RepositoriesApi.md#get_v5_repos_owner_repo_keys_available) | **GET** /v5/repos/{owner}/{repo}/keys/available | 获取仓库可部署的公钥
[**get_v5_repos_owner_repo_keys_id**](RepositoriesApi.md#get_v5_repos_owner_repo_keys_id) | **GET** /v5/repos/{owner}/{repo}/keys/{id} | 获取仓库的单个公钥
[**get_v5_repos_owner_repo_pages**](RepositoriesApi.md#get_v5_repos_owner_repo_pages) | **GET** /v5/repos/{owner}/{repo}/pages | 获取Pages信息
[**get_v5_repos_owner_repo_readme**](RepositoriesApi.md#get_v5_repos_owner_repo_readme) | **GET** /v5/repos/{owner}/{repo}/readme | 获取仓库README
[**get_v5_repos_owner_repo_releases**](RepositoriesApi.md#get_v5_repos_owner_repo_releases) | **GET** /v5/repos/{owner}/{repo}/releases | 获取仓库的所有Releases
[**get_v5_repos_owner_repo_releases_id**](RepositoriesApi.md#get_v5_repos_owner_repo_releases_id) | **GET** /v5/repos/{owner}/{repo}/releases/{id} | 获取仓库的单个Releases
[**get_v5_repos_owner_repo_releases_latest**](RepositoriesApi.md#get_v5_repos_owner_repo_releases_latest) | **GET** /v5/repos/{owner}/{repo}/releases/latest | 获取仓库的最后更新的Release
[**get_v5_repos_owner_repo_releases_tags_tag**](RepositoriesApi.md#get_v5_repos_owner_repo_releases_tags_tag) | **GET** /v5/repos/{owner}/{repo}/releases/tags/{tag} | 根据Tag名称获取仓库的Release
[**get_v5_repos_owner_repo_tags**](RepositoriesApi.md#get_v5_repos_owner_repo_tags) | **GET** /v5/repos/{owner}/{repo}/tags | 列出仓库所有的tags
[**get_v5_user_repos**](RepositoriesApi.md#get_v5_user_repos) | **GET** /v5/user/repos | 列出授权用户的所有仓库
[**get_v5_users_username_repos**](RepositoriesApi.md#get_v5_users_username_repos) | **GET** /v5/users/{username}/repos | 获取某个用户的公开仓库
[**patch_v5_repos_owner_repo**](RepositoriesApi.md#patch_v5_repos_owner_repo) | **PATCH** /v5/repos/{owner}/{repo} | 更新仓库设置
[**patch_v5_repos_owner_repo_comments_id**](RepositoriesApi.md#patch_v5_repos_owner_repo_comments_id) | **PATCH** /v5/repos/{owner}/{repo}/comments/{id} | 更新Commit评论
[**patch_v5_repos_owner_repo_releases_id**](RepositoriesApi.md#patch_v5_repos_owner_repo_releases_id) | **PATCH** /v5/repos/{owner}/{repo}/releases/{id} | 更新仓库Release
[**post_v5_enterprises_enterprise_repos**](RepositoriesApi.md#post_v5_enterprises_enterprise_repos) | **POST** /v5/enterprises/{enterprise}/repos | 创建企业仓库
[**post_v5_orgs_org_repos**](RepositoriesApi.md#post_v5_orgs_org_repos) | **POST** /v5/orgs/{org}/repos | 创建组织仓库
[**post_v5_repos_owner_repo_branches**](RepositoriesApi.md#post_v5_repos_owner_repo_branches) | **POST** /v5/repos/{owner}/{repo}/branches | 创建分支
[**post_v5_repos_owner_repo_commits_sha_comments**](RepositoriesApi.md#post_v5_repos_owner_repo_commits_sha_comments) | **POST** /v5/repos/{owner}/{repo}/commits/{sha}/comments | 创建Commit评论
[**post_v5_repos_owner_repo_contents_path**](RepositoriesApi.md#post_v5_repos_owner_repo_contents_path) | **POST** /v5/repos/{owner}/{repo}/contents/{path} | 新建文件
[**post_v5_repos_owner_repo_forks**](RepositoriesApi.md#post_v5_repos_owner_repo_forks) | **POST** /v5/repos/{owner}/{repo}/forks | Fork一个仓库
[**post_v5_repos_owner_repo_keys**](RepositoriesApi.md#post_v5_repos_owner_repo_keys) | **POST** /v5/repos/{owner}/{repo}/keys | 为仓库添加公钥
[**post_v5_repos_owner_repo_pages_builds**](RepositoriesApi.md#post_v5_repos_owner_repo_pages_builds) | **POST** /v5/repos/{owner}/{repo}/pages/builds | 请求建立Pages
[**post_v5_repos_owner_repo_releases**](RepositoriesApi.md#post_v5_repos_owner_repo_releases) | **POST** /v5/repos/{owner}/{repo}/releases | 创建仓库Release
[**post_v5_user_repos**](RepositoriesApi.md#post_v5_user_repos) | **POST** /v5/user/repos | 创建一个仓库
[**put_v5_repos_owner_repo_branches_branch_protection**](RepositoriesApi.md#put_v5_repos_owner_repo_branches_branch_protection) | **PUT** /v5/repos/{owner}/{repo}/branches/{branch}/protection | 设置分支保护
[**put_v5_repos_owner_repo_clear**](RepositoriesApi.md#put_v5_repos_owner_repo_clear) | **PUT** /v5/repos/{owner}/{repo}/clear | 清空一个仓库
[**put_v5_repos_owner_repo_collaborators_username**](RepositoriesApi.md#put_v5_repos_owner_repo_collaborators_username) | **PUT** /v5/repos/{owner}/{repo}/collaborators/{username} | 添加仓库成员
[**put_v5_repos_owner_repo_contents_path**](RepositoriesApi.md#put_v5_repos_owner_repo_contents_path) | **PUT** /v5/repos/{owner}/{repo}/contents/{path} | 更新文件
[**put_v5_repos_owner_repo_keys_enable_id**](RepositoriesApi.md#put_v5_repos_owner_repo_keys_enable_id) | **PUT** /v5/repos/{owner}/{repo}/keys/enable/{id} | 启用仓库公钥
[**put_v5_repos_owner_repo_reviewer**](RepositoriesApi.md#put_v5_repos_owner_repo_reviewer) | **PUT** /v5/repos/{owner}/{repo}/reviewer | 修改代码审查设置


# **delete_v5_repos_owner_repo**
> delete_v5_repos_owner_repo(owner, repo, access_token=access_token)

删除一个仓库

删除一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除一个仓库
    api_instance.delete_v5_repos_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_v5_repos_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_branches_branch_protection**
> delete_v5_repos_owner_repo_branches_branch_protection(owner, repo, branch, access_token=access_token)

取消保护分支的设置

取消保护分支的设置

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
branch = 'branch_example' # str | 分支名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消保护分支的设置
    api_instance.delete_v5_repos_owner_repo_branches_branch_protection(owner, repo, branch, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_v5_repos_owner_repo_branches_branch_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **branch** | **str**| 分支名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_collaborators_username**
> delete_v5_repos_owner_repo_collaborators_username(owner, repo, username, access_token=access_token)

移除仓库成员

移除仓库成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 移除仓库成员
    api_instance.delete_v5_repos_owner_repo_collaborators_username(owner, repo, username, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_v5_repos_owner_repo_collaborators_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_comments_id**
> delete_v5_repos_owner_repo_comments_id(owner, repo, id, access_token=access_token)

删除Commit评论

删除Commit评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除Commit评论
    api_instance.delete_v5_repos_owner_repo_comments_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_v5_repos_owner_repo_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_contents_path**
> CommitContent delete_v5_repos_owner_repo_contents_path(owner, repo, path, sha, message, access_token=access_token, branch=branch, committer_name=committer_name, committer_email=committer_email, author_name=author_name, author_email=author_email)

删除文件

删除文件

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
path = 'path_example' # str | 文件的路径
sha = 'sha_example' # str | 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取
message = 'message_example' # str | 提交信息
access_token = 'access_token_example' # str | 用户授权码 (optional)
branch = 'branch_example' # str | 分支名称。默认为仓库对默认分支 (optional)
committer_name = 'committer_name_example' # str | Committer的名字，默认为当前用户的名字 (optional)
committer_email = 'committer_email_example' # str | Committer的邮箱，默认为当前用户的邮箱 (optional)
author_name = 'author_name_example' # str | Author的名字，默认为当前用户的名字 (optional)
author_email = 'author_email_example' # str | Author的邮箱，默认为当前用户的邮箱 (optional)

try:
    # 删除文件
    api_response = api_instance.delete_v5_repos_owner_repo_contents_path(owner, repo, path, sha, message, access_token=access_token, branch=branch, committer_name=committer_name, committer_email=committer_email, author_name=author_name, author_email=author_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_v5_repos_owner_repo_contents_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **path** | **str**| 文件的路径 | 
 **sha** | **str**| 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取 | 
 **message** | **str**| 提交信息 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **branch** | **str**| 分支名称。默认为仓库对默认分支 | [optional] 
 **committer_name** | **str**| Committer的名字，默认为当前用户的名字 | [optional] 
 **committer_email** | **str**| Committer的邮箱，默认为当前用户的邮箱 | [optional] 
 **author_name** | **str**| Author的名字，默认为当前用户的名字 | [optional] 
 **author_email** | **str**| Author的邮箱，默认为当前用户的邮箱 | [optional] 

### Return type

[**CommitContent**](CommitContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_keys_enable_id**
> delete_v5_repos_owner_repo_keys_enable_id(owner, repo, id, access_token=access_token)

停用仓库公钥

停用仓库公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 停用仓库公钥
    api_instance.delete_v5_repos_owner_repo_keys_enable_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_v5_repos_owner_repo_keys_enable_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_keys_id**
> delete_v5_repos_owner_repo_keys_id(owner, repo, id, access_token=access_token)

删除一个仓库公钥

删除一个仓库公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除一个仓库公钥
    api_instance.delete_v5_repos_owner_repo_keys_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_v5_repos_owner_repo_keys_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_releases_id**
> delete_v5_repos_owner_repo_releases_id(owner, repo, id, access_token=access_token)

删除仓库Release

删除仓库Release

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除仓库Release
    api_instance.delete_v5_repos_owner_repo_releases_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_v5_repos_owner_repo_releases_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**|  | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_repos**
> Project get_v5_enterprises_enterprise_repos(enterprise, access_token=access_token, type=type, direct=direct, page=page, per_page=per_page)

获取企业的所有仓库

获取企业的所有仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
type = 'all' # str | 筛选仓库的类型，可以是 all, public, internal, private。默认: all (optional) (default to all)
direct = true # bool | 只获取直属仓库，默认: false (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取企业的所有仓库
    api_response = api_instance.get_v5_enterprises_enterprise_repos(enterprise, access_token=access_token, type=type, direct=direct, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_enterprises_enterprise_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **type** | **str**| 筛选仓库的类型，可以是 all, public, internal, private。默认: all | [optional] [default to all]
 **direct** | **bool**| 只获取直属仓库，默认: false | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_orgs_org_repos**
> list[Project] get_v5_orgs_org_repos(org, access_token=access_token, type=type, page=page, per_page=per_page)

获取一个组织的仓库

获取一个组织的仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
type = 'all' # str | 筛选仓库的类型，可以是 all, public, private。默认: all (optional) (default to all)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取一个组织的仓库
    api_response = api_instance.get_v5_orgs_org_repos(org, access_token=access_token, type=type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_orgs_org_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **type** | **str**| 筛选仓库的类型，可以是 all, public, private。默认: all | [optional] [default to all]
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo**
> Project get_v5_repos_owner_repo(owner, repo, access_token=access_token)

获取用户的某个仓库

获取用户的某个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取用户的某个仓库
    api_response = api_instance.get_v5_repos_owner_repo(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_branches**
> list[Branch] get_v5_repos_owner_repo_branches(owner, repo, access_token=access_token)

获取所有分支

获取所有分支

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取所有分支
    api_response = api_instance.get_v5_repos_owner_repo_branches(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**list[Branch]**](Branch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_branches_branch**
> Branch get_v5_repos_owner_repo_branches_branch(owner, repo, branch, access_token=access_token)

获取单个分支

获取单个分支

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
branch = 'branch_example' # str | 分支名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取单个分支
    api_response = api_instance.get_v5_repos_owner_repo_branches_branch(owner, repo, branch, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_branches_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **branch** | **str**| 分支名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Branch**](Branch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_collaborators**
> list[ProjectMember] get_v5_repos_owner_repo_collaborators(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取仓库的所有成员

获取仓库的所有成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取仓库的所有成员
    api_response = api_instance.get_v5_repos_owner_repo_collaborators(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_collaborators: %s\n" % e)
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

[**list[ProjectMember]**](ProjectMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_collaborators_username**
> get_v5_repos_owner_repo_collaborators_username(owner, repo, username, access_token=access_token)

判断用户是否为仓库成员

判断用户是否为仓库成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 判断用户是否为仓库成员
    api_instance.get_v5_repos_owner_repo_collaborators_username(owner, repo, username, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_collaborators_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_collaborators_username_permission**
> ProjectMemberPermission get_v5_repos_owner_repo_collaborators_username_permission(owner, repo, username, access_token=access_token)

查看仓库成员的权限

查看仓库成员的权限

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 查看仓库成员的权限
    api_response = api_instance.get_v5_repos_owner_repo_collaborators_username_permission(owner, repo, username, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_collaborators_username_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**ProjectMemberPermission**](ProjectMemberPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_comments**
> Note get_v5_repos_owner_repo_comments(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取仓库的Commit评论

获取仓库的Commit评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取仓库的Commit评论
    api_response = api_instance.get_v5_repos_owner_repo_comments(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_comments: %s\n" % e)
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

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_comments_id**
> Note get_v5_repos_owner_repo_comments_id(owner, repo, id, access_token=access_token)

获取仓库的某条Commit评论

获取仓库的某条Commit评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的某条Commit评论
    api_response = api_instance.get_v5_repos_owner_repo_comments_id(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_commits**
> list[RepoCommit] get_v5_repos_owner_repo_commits(owner, repo, access_token=access_token, sha=sha, path=path, author=author, since=since, until=until, page=page, per_page=per_page)

仓库的所有提交

仓库的所有提交

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
sha = 'sha_example' # str | 提交起始的SHA值或者分支名. 默认: 仓库的默认分支 (optional)
path = 'path_example' # str | 包含该文件的提交 (optional)
author = 'author_example' # str | 提交作者的邮箱或个人空间地址(username/login) (optional)
since = 'since_example' # str | 提交的起始时间，时间格式为 ISO 8601 (optional)
until = 'until_example' # str | 提交的最后时间，时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 仓库的所有提交
    api_response = api_instance.get_v5_repos_owner_repo_commits(owner, repo, access_token=access_token, sha=sha, path=path, author=author, since=since, until=until, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_commits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sha** | **str**| 提交起始的SHA值或者分支名. 默认: 仓库的默认分支 | [optional] 
 **path** | **str**| 包含该文件的提交 | [optional] 
 **author** | **str**| 提交作者的邮箱或个人空间地址(username/login) | [optional] 
 **since** | **str**| 提交的起始时间，时间格式为 ISO 8601 | [optional] 
 **until** | **str**| 提交的最后时间，时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[RepoCommit]**](RepoCommit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_commits_ref_comments**
> Note get_v5_repos_owner_repo_commits_ref_comments(owner, repo, ref, access_token=access_token, page=page, per_page=per_page)

获取单个Commit的评论

获取单个Commit的评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
ref = 'ref_example' # str | Commit的Reference
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取单个Commit的评论
    api_response = api_instance.get_v5_repos_owner_repo_commits_ref_comments(owner, repo, ref, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_commits_ref_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **ref** | **str**| Commit的Reference | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_commits_sha**
> RepoCommit get_v5_repos_owner_repo_commits_sha(owner, repo, sha, access_token=access_token)

仓库的某个提交

仓库的某个提交

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
sha = 'sha_example' # str | 提交的SHA值或者分支名
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 仓库的某个提交
    api_response = api_instance.get_v5_repos_owner_repo_commits_sha(owner, repo, sha, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_commits_sha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **sha** | **str**| 提交的SHA值或者分支名 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**RepoCommit**](RepoCommit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_compare_base___head**
> Compare get_v5_repos_owner_repo_compare_base___head(owner, repo, base, head, access_token=access_token)

两个Commits之间对比的版本差异

两个Commits之间对比的版本差异

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
base = 'base_example' # str | Commit提交的SHA值或者分支名作为对比起点
head = 'head_example' # str | Commit提交的SHA值或者分支名作为对比终点
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 两个Commits之间对比的版本差异
    api_response = api_instance.get_v5_repos_owner_repo_compare_base___head(owner, repo, base, head, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_compare_base___head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **base** | **str**| Commit提交的SHA值或者分支名作为对比起点 | 
 **head** | **str**| Commit提交的SHA值或者分支名作为对比终点 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Compare**](Compare.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_contents_path**
> Content get_v5_repos_owner_repo_contents_path(owner, repo, path, access_token=access_token, ref=ref)

获取仓库具体路径下的内容

获取仓库具体路径下的内容

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
path = 'path_example' # str | 文件的路径
access_token = 'access_token_example' # str | 用户授权码 (optional)
ref = 'ref_example' # str | 分支、tag或commit。默认: 仓库的默认分支(通常是master) (optional)

try:
    # 获取仓库具体路径下的内容
    api_response = api_instance.get_v5_repos_owner_repo_contents_path(owner, repo, path, access_token=access_token, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_contents_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **path** | **str**| 文件的路径 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **ref** | **str**| 分支、tag或commit。默认: 仓库的默认分支(通常是master) | [optional] 

### Return type

[**Content**](Content.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_contributors**
> Contributor get_v5_repos_owner_repo_contributors(owner, repo, access_token=access_token)

获取仓库贡献者

获取仓库贡献者

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库贡献者
    api_response = api_instance.get_v5_repos_owner_repo_contributors(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_contributors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Contributor**](Contributor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_forks**
> Project get_v5_repos_owner_repo_forks(owner, repo, access_token=access_token, sort=sort, page=page, per_page=per_page)

查看仓库的Forks

查看仓库的Forks

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'newest' # str | 排序方式: fork的时间(newest, oldest)，star的人数(stargazers) (optional) (default to newest)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 查看仓库的Forks
    api_response = api_instance.get_v5_repos_owner_repo_forks(owner, repo, access_token=access_token, sort=sort, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_forks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 排序方式: fork的时间(newest, oldest)，star的人数(stargazers) | [optional] [default to newest]
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_keys**
> list[SSHKey] get_v5_repos_owner_repo_keys(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取仓库已部署的公钥

获取仓库已部署的公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取仓库已部署的公钥
    api_response = api_instance.get_v5_repos_owner_repo_keys(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_keys: %s\n" % e)
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

[**list[SSHKey]**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_keys_available**
> list[SSHKeyBasic] get_v5_repos_owner_repo_keys_available(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取仓库可部署的公钥

获取仓库可部署的公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取仓库可部署的公钥
    api_response = api_instance.get_v5_repos_owner_repo_keys_available(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_keys_available: %s\n" % e)
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

[**list[SSHKeyBasic]**](SSHKeyBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_keys_id**
> SSHKey get_v5_repos_owner_repo_keys_id(owner, repo, id, access_token=access_token)

获取仓库的单个公钥

获取仓库的单个公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的单个公钥
    api_response = api_instance.get_v5_repos_owner_repo_keys_id(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_keys_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pages**
> get_v5_repos_owner_repo_pages(owner, repo, access_token=access_token)

获取Pages信息

获取Pages信息

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取Pages信息
    api_instance.get_v5_repos_owner_repo_pages(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_readme**
> Content get_v5_repos_owner_repo_readme(owner, repo, access_token=access_token, ref=ref)

获取仓库README

获取仓库README

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
ref = 'ref_example' # str | 分支、tag或commit。默认: 仓库的默认分支(通常是master) (optional)

try:
    # 获取仓库README
    api_response = api_instance.get_v5_repos_owner_repo_readme(owner, repo, access_token=access_token, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_readme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **ref** | **str**| 分支、tag或commit。默认: 仓库的默认分支(通常是master) | [optional] 

### Return type

[**Content**](Content.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_releases**
> list[Release] get_v5_repos_owner_repo_releases(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取仓库的所有Releases

获取仓库的所有Releases

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取仓库的所有Releases
    api_response = api_instance.get_v5_repos_owner_repo_releases(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_releases: %s\n" % e)
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

[**list[Release]**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_releases_id**
> Release get_v5_repos_owner_repo_releases_id(owner, repo, id, access_token=access_token)

获取仓库的单个Releases

获取仓库的单个Releases

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 发行版本的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的单个Releases
    api_response = api_instance.get_v5_repos_owner_repo_releases_id(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_releases_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 发行版本的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_releases_latest**
> Release get_v5_repos_owner_repo_releases_latest(owner, repo, access_token=access_token)

获取仓库的最后更新的Release

获取仓库的最后更新的Release

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的最后更新的Release
    api_response = api_instance.get_v5_repos_owner_repo_releases_latest(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_releases_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_releases_tags_tag**
> Release get_v5_repos_owner_repo_releases_tags_tag(owner, repo, tag, access_token=access_token)

根据Tag名称获取仓库的Release

根据Tag名称获取仓库的Release

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
tag = 'tag_example' # str | Tag 名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 根据Tag名称获取仓库的Release
    api_response = api_instance.get_v5_repos_owner_repo_releases_tags_tag(owner, repo, tag, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_releases_tags_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **tag** | **str**| Tag 名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_tags**
> Tag get_v5_repos_owner_repo_tags(owner, repo, access_token=access_token)

列出仓库所有的tags

列出仓库所有的tags

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 列出仓库所有的tags
    api_response = api_instance.get_v5_repos_owner_repo_tags(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_repos_owner_repo_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_repos**
> Project get_v5_user_repos(access_token=access_token, visibility=visibility, affiliation=affiliation, type=type, sort=sort, direction=direction, page=page, per_page=per_page)

列出授权用户的所有仓库

列出授权用户的所有仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
visibility = 'visibility_example' # str | 公开(public)、私有(private)或者所有(all)，默认: 所有(all) (optional)
affiliation = 'affiliation_example' # str | owner(授权用户拥有的仓库)、collaborator(授权用户为仓库成员)、organization_member(授权用户为仓库所在组织并有访问仓库权限)、enterprise_member(授权用户所在企业并有访问仓库权限)、admin(所有有权限的，包括所管理的组织中所有仓库、所管理的企业的所有仓库)。                    可以用逗号分隔符组合。如: owner, organization_member 或 owner, collaborator, organization_member (optional)
type = 'type_example' # str | 筛选用户仓库: 其创建(owner)、个人(personal)、其为成员(member)、公开(public)、私有(private)，不能与 visibility 或 affiliation 参数一并使用，否则会报 422 错误 (optional)
sort = 'full_name' # str | 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name (optional) (default to full_name)
direction = 'direction_example' # str | 如果sort参数为full_name，用升序(asc)。否则降序(desc) (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户的所有仓库
    api_response = api_instance.get_v5_user_repos(access_token=access_token, visibility=visibility, affiliation=affiliation, type=type, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_user_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **visibility** | **str**| 公开(public)、私有(private)或者所有(all)，默认: 所有(all) | [optional] 
 **affiliation** | **str**| owner(授权用户拥有的仓库)、collaborator(授权用户为仓库成员)、organization_member(授权用户为仓库所在组织并有访问仓库权限)、enterprise_member(授权用户所在企业并有访问仓库权限)、admin(所有有权限的，包括所管理的组织中所有仓库、所管理的企业的所有仓库)。                    可以用逗号分隔符组合。如: owner, organization_member 或 owner, collaborator, organization_member | [optional] 
 **type** | **str**| 筛选用户仓库: 其创建(owner)、个人(personal)、其为成员(member)、公开(public)、私有(private)，不能与 visibility 或 affiliation 参数一并使用，否则会报 422 错误 | [optional] 
 **sort** | **str**| 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name | [optional] [default to full_name]
 **direction** | **str**| 如果sort参数为full_name，用升序(asc)。否则降序(desc) | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_repos**
> Project get_v5_users_username_repos(username, access_token=access_token, type=type, sort=sort, direction=direction, page=page, per_page=per_page)

获取某个用户的公开仓库

获取某个用户的公开仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
type = 'all' # str | 用户创建的仓库(owner)，用户个人仓库(personal)，用户为仓库成员(member)，所有(all)。默认: 所有(all) (optional) (default to all)
sort = 'full_name' # str | 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name (optional) (default to full_name)
direction = 'direction_example' # str | 如果sort参数为full_name，用升序(asc)。否则降序(desc) (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取某个用户的公开仓库
    api_response = api_instance.get_v5_users_username_repos(username, access_token=access_token, type=type, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_v5_users_username_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **type** | **str**| 用户创建的仓库(owner)，用户个人仓库(personal)，用户为仓库成员(member)，所有(all)。默认: 所有(all) | [optional] [default to all]
 **sort** | **str**| 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name | [optional] [default to full_name]
 **direction** | **str**| 如果sort参数为full_name，用升序(asc)。否则降序(desc) | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo**
> Project patch_v5_repos_owner_repo(owner, repo, body)

更新仓库设置

更新仓库设置

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = gitee.RepoPatchParam() # RepoPatchParam | repo patch param

try:
    # 更新仓库设置
    api_response = api_instance.patch_v5_repos_owner_repo(owner, repo, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->patch_v5_repos_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**RepoPatchParam**](RepoPatchParam.md)| repo patch param | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_comments_id**
> Note patch_v5_repos_owner_repo_comments_id(owner, repo, id, body, access_token=access_token)

更新Commit评论

更新Commit评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
body = 'body_example' # str | 评论的内容
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 更新Commit评论
    api_response = api_instance.patch_v5_repos_owner_repo_comments_id(owner, repo, id, body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->patch_v5_repos_owner_repo_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **body** | **str**| 评论的内容 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_releases_id**
> Release patch_v5_repos_owner_repo_releases_id(owner, repo, tag_name, name, body, id, access_token=access_token, prerelease=prerelease)

更新仓库Release

更新仓库Release

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
tag_name = 'tag_name_example' # str | Tag 名称, 提倡以v字母为前缀做为Release名称，例如v1.0或者v2.3.4
name = 'name_example' # str | Release 名称
body = 'body_example' # str | Release 描述
id = 56 # int | 
access_token = 'access_token_example' # str | 用户授权码 (optional)
prerelease = true # bool | 是否为预览版本。默认: false（非预览版本） (optional)

try:
    # 更新仓库Release
    api_response = api_instance.patch_v5_repos_owner_repo_releases_id(owner, repo, tag_name, name, body, id, access_token=access_token, prerelease=prerelease)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->patch_v5_repos_owner_repo_releases_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **tag_name** | **str**| Tag 名称, 提倡以v字母为前缀做为Release名称，例如v1.0或者v2.3.4 | 
 **name** | **str**| Release 名称 | 
 **body** | **str**| Release 描述 | 
 **id** | **int**|  | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prerelease** | **bool**| 是否为预览版本。默认: false（非预览版本） | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_enterprises_enterprise_repos**
> Project post_v5_enterprises_enterprise_repos(name, enterprise, access_token=access_token, description=description, homepage=homepage, has_issues=has_issues, has_wiki=has_wiki, can_comment=can_comment, auto_init=auto_init, gitignore_template=gitignore_template, license_template=license_template, private=private, outsourced=outsourced, project_creator=project_creator, members=members)

创建企业仓库

创建企业仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
name = 'name_example' # str | 仓库名称
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
description = 'description_example' # str | 仓库描述 (optional)
homepage = 'homepage_example' # str | 主页(eg: https://gitee.com) (optional)
has_issues = true # bool | 允许提Issue与否。默认: 允许(true) (optional) (default to true)
has_wiki = true # bool | 提供Wiki与否。默认: 提供(true) (optional) (default to true)
can_comment = true # bool | 允许用户对仓库进行评论。默认： 允许(true) (optional) (default to true)
auto_init = true # bool | 值为true时则会用README初始化仓库。默认: 不初始化(false) (optional)
gitignore_template = 'gitignore_template_example' # str | Git Ingore模版 (optional)
license_template = 'license_template_example' # str | License模版 (optional)
private = 0 # int | 仓库开源类型。0(私有), 1(外部开源), 2(内部开源)。默认: 0 (optional) (default to 0)
outsourced = true # bool | 值为true值为外包仓库, false值为内部仓库。默认: 内部仓库(false) (optional)
project_creator = 'project_creator_example' # str | 负责人的username (optional)
members = 'members_example' # str | 用逗号分开的仓库成员。如: member1,member2 (optional)

try:
    # 创建企业仓库
    api_response = api_instance.post_v5_enterprises_enterprise_repos(name, enterprise, access_token=access_token, description=description, homepage=homepage, has_issues=has_issues, has_wiki=has_wiki, can_comment=can_comment, auto_init=auto_init, gitignore_template=gitignore_template, license_template=license_template, private=private, outsourced=outsourced, project_creator=project_creator, members=members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_enterprises_enterprise_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| 仓库名称 | 
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **description** | **str**| 仓库描述 | [optional] 
 **homepage** | **str**| 主页(eg: https://gitee.com) | [optional] 
 **has_issues** | **bool**| 允许提Issue与否。默认: 允许(true) | [optional] [default to true]
 **has_wiki** | **bool**| 提供Wiki与否。默认: 提供(true) | [optional] [default to true]
 **can_comment** | **bool**| 允许用户对仓库进行评论。默认： 允许(true) | [optional] [default to true]
 **auto_init** | **bool**| 值为true时则会用README初始化仓库。默认: 不初始化(false) | [optional] 
 **gitignore_template** | **str**| Git Ingore模版 | [optional] 
 **license_template** | **str**| License模版 | [optional] 
 **private** | **int**| 仓库开源类型。0(私有), 1(外部开源), 2(内部开源)。默认: 0 | [optional] [default to 0]
 **outsourced** | **bool**| 值为true值为外包仓库, false值为内部仓库。默认: 内部仓库(false) | [optional] 
 **project_creator** | **str**| 负责人的username | [optional] 
 **members** | **str**| 用逗号分开的仓库成员。如: member1,member2 | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_orgs_org_repos**
> Project post_v5_orgs_org_repos(org, body)

创建组织仓库

创建组织仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
org = 'org_example' # str | 组织的路径(path/login)
body = gitee.RepositoryPostParam() # RepositoryPostParam | Repositorie 内容

try:
    # 创建组织仓库
    api_response = api_instance.post_v5_orgs_org_repos(org, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_orgs_org_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **body** | [**RepositoryPostParam**](RepositoryPostParam.md)| Repositorie 内容 | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_branches**
> CompleteBranch post_v5_repos_owner_repo_branches(owner, repo, body)

创建分支

创建分支

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = gitee.CreateBranchParam() # CreateBranchParam | 新建分支内容

try:
    # 创建分支
    api_response = api_instance.post_v5_repos_owner_repo_branches(owner, repo, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_repos_owner_repo_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**CreateBranchParam**](CreateBranchParam.md)| 新建分支内容 | 

### Return type

[**CompleteBranch**](CompleteBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_commits_sha_comments**
> Note post_v5_repos_owner_repo_commits_sha_comments(owner, repo, sha, body, access_token=access_token, path=path, position=position)

创建Commit评论

创建Commit评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
sha = 'sha_example' # str | 评论的sha值
body = 'body_example' # str | 评论的内容
access_token = 'access_token_example' # str | 用户授权码 (optional)
path = 'path_example' # str | 文件的相对路径 (optional)
position = 56 # int | Diff的相对行数 (optional)

try:
    # 创建Commit评论
    api_response = api_instance.post_v5_repos_owner_repo_commits_sha_comments(owner, repo, sha, body, access_token=access_token, path=path, position=position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_repos_owner_repo_commits_sha_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **sha** | **str**| 评论的sha值 | 
 **body** | **str**| 评论的内容 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **path** | **str**| 文件的相对路径 | [optional] 
 **position** | **int**| Diff的相对行数 | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_contents_path**
> CommitContent post_v5_repos_owner_repo_contents_path(owner, repo, path, body)

新建文件

新建文件

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
path = 'path_example' # str | 文件的路径
body = gitee.NewFileParam() # NewFileParam | 描述文件信息

try:
    # 新建文件
    api_response = api_instance.post_v5_repos_owner_repo_contents_path(owner, repo, path, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_repos_owner_repo_contents_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **path** | **str**| 文件的路径 | 
 **body** | [**NewFileParam**](NewFileParam.md)| 描述文件信息 | 

### Return type

[**CommitContent**](CommitContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_forks**
> Project post_v5_repos_owner_repo_forks(owner, repo, access_token=access_token, organization=organization)

Fork一个仓库

Fork一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
organization = 'organization_example' # str | 组织空间地址，不填写默认Fork到用户个人空间地址 (optional)

try:
    # Fork一个仓库
    api_response = api_instance.post_v5_repos_owner_repo_forks(owner, repo, access_token=access_token, organization=organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_repos_owner_repo_forks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **organization** | **str**| 组织空间地址，不填写默认Fork到用户个人空间地址 | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_keys**
> SSHKey post_v5_repos_owner_repo_keys(owner, repo, key, title, access_token=access_token)

为仓库添加公钥

为仓库添加公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
key = 'key_example' # str | 公钥内容
title = 'title_example' # str | 公钥名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 为仓库添加公钥
    api_response = api_instance.post_v5_repos_owner_repo_keys(owner, repo, key, title, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_repos_owner_repo_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **key** | **str**| 公钥内容 | 
 **title** | **str**| 公钥名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_pages_builds**
> post_v5_repos_owner_repo_pages_builds(owner, repo, access_token=access_token)

请求建立Pages

请求建立Pages

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 请求建立Pages
    api_instance.post_v5_repos_owner_repo_pages_builds(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_repos_owner_repo_pages_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_releases**
> Release post_v5_repos_owner_repo_releases(owner, repo, tag_name, name, body, target_commitish, access_token=access_token, prerelease=prerelease)

创建仓库Release

创建仓库Release

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
tag_name = 'tag_name_example' # str | Tag 名称, 提倡以v字母为前缀做为Release名称，例如v1.0或者v2.3.4
name = 'name_example' # str | Release 名称
body = 'body_example' # str | Release 描述
target_commitish = 'target_commitish_example' # str | 分支名称或者commit SHA, 默认是当前默认分支
access_token = 'access_token_example' # str | 用户授权码 (optional)
prerelease = true # bool | 是否为预览版本。默认: false（非预览版本） (optional)

try:
    # 创建仓库Release
    api_response = api_instance.post_v5_repos_owner_repo_releases(owner, repo, tag_name, name, body, target_commitish, access_token=access_token, prerelease=prerelease)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_repos_owner_repo_releases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **tag_name** | **str**| Tag 名称, 提倡以v字母为前缀做为Release名称，例如v1.0或者v2.3.4 | 
 **name** | **str**| Release 名称 | 
 **body** | **str**| Release 描述 | 
 **target_commitish** | **str**| 分支名称或者commit SHA, 默认是当前默认分支 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prerelease** | **bool**| 是否为预览版本。默认: false（非预览版本） | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_user_repos**
> Project post_v5_user_repos(name, access_token=access_token, description=description, homepage=homepage, has_issues=has_issues, has_wiki=has_wiki, can_comment=can_comment, auto_init=auto_init, gitignore_template=gitignore_template, license_template=license_template, private=private)

创建一个仓库

创建一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
name = 'name_example' # str | 仓库名称
access_token = 'access_token_example' # str | 用户授权码 (optional)
description = 'description_example' # str | 仓库描述 (optional)
homepage = 'homepage_example' # str | 主页(eg: https://gitee.com) (optional)
has_issues = true # bool | 允许提Issue与否。默认: 允许(true) (optional) (default to true)
has_wiki = true # bool | 提供Wiki与否。默认: 提供(true) (optional) (default to true)
can_comment = true # bool | 允许用户对仓库进行评论。默认: 允许(true) (optional) (default to true)
auto_init = true # bool | 值为true时则会用README初始化仓库。默认: 不初始化(false) (optional)
gitignore_template = 'gitignore_template_example' # str | Git Ingore模版 (optional)
license_template = 'license_template_example' # str | License模版 (optional)
private = true # bool | 仓库公开或私有。默认: 公开(false) (optional)

try:
    # 创建一个仓库
    api_response = api_instance.post_v5_user_repos(name, access_token=access_token, description=description, homepage=homepage, has_issues=has_issues, has_wiki=has_wiki, can_comment=can_comment, auto_init=auto_init, gitignore_template=gitignore_template, license_template=license_template, private=private)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_v5_user_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| 仓库名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **description** | **str**| 仓库描述 | [optional] 
 **homepage** | **str**| 主页(eg: https://gitee.com) | [optional] 
 **has_issues** | **bool**| 允许提Issue与否。默认: 允许(true) | [optional] [default to true]
 **has_wiki** | **bool**| 提供Wiki与否。默认: 提供(true) | [optional] [default to true]
 **can_comment** | **bool**| 允许用户对仓库进行评论。默认: 允许(true) | [optional] [default to true]
 **auto_init** | **bool**| 值为true时则会用README初始化仓库。默认: 不初始化(false) | [optional] 
 **gitignore_template** | **str**| Git Ingore模版 | [optional] 
 **license_template** | **str**| License模版 | [optional] 
 **private** | **bool**| 仓库公开或私有。默认: 公开(false) | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_branches_branch_protection**
> CompleteBranch put_v5_repos_owner_repo_branches_branch_protection(owner, repo, branch, body)

设置分支保护

设置分支保护

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
branch = 'branch_example' # str | 分支名称
body = gitee.BranchProtectionPutParam() # BranchProtectionPutParam | 设置分支保护参数

try:
    # 设置分支保护
    api_response = api_instance.put_v5_repos_owner_repo_branches_branch_protection(owner, repo, branch, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_v5_repos_owner_repo_branches_branch_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **branch** | **str**| 分支名称 | 
 **body** | [**BranchProtectionPutParam**](BranchProtectionPutParam.md)| 设置分支保护参数 | 

### Return type

[**CompleteBranch**](CompleteBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_clear**
> put_v5_repos_owner_repo_clear(owner, repo, access_token=access_token)

清空一个仓库

清空一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 清空一个仓库
    api_instance.put_v5_repos_owner_repo_clear(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_v5_repos_owner_repo_clear: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_collaborators_username**
> ProjectMember put_v5_repos_owner_repo_collaborators_username(owner, repo, username, body)

添加仓库成员

添加仓库成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
username = 'username_example' # str | 用户名(username/login)
body = gitee.ProjectMemberPutParam() # ProjectMemberPutParam | 仓库成员内容

try:
    # 添加仓库成员
    api_response = api_instance.put_v5_repos_owner_repo_collaborators_username(owner, repo, username, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_v5_repos_owner_repo_collaborators_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **username** | **str**| 用户名(username/login) | 
 **body** | [**ProjectMemberPutParam**](ProjectMemberPutParam.md)| 仓库成员内容 | 

### Return type

[**ProjectMember**](ProjectMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_contents_path**
> CommitContent put_v5_repos_owner_repo_contents_path(owner, repo, path, content, sha, message, access_token=access_token, branch=branch, committer_name=committer_name, committer_email=committer_email, author_name=author_name, author_email=author_email)

更新文件

更新文件

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
path = 'path_example' # str | 文件的路径
content = 'content_example' # str | 文件内容, 要用 base64 编码
sha = 'sha_example' # str | 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取
message = 'message_example' # str | 提交信息
access_token = 'access_token_example' # str | 用户授权码 (optional)
branch = 'branch_example' # str | 分支名称。默认为仓库对默认分支 (optional)
committer_name = 'committer_name_example' # str | Committer的名字，默认为当前用户的名字 (optional)
committer_email = 'committer_email_example' # str | Committer的邮箱，默认为当前用户的邮箱 (optional)
author_name = 'author_name_example' # str | Author的名字，默认为当前用户的名字 (optional)
author_email = 'author_email_example' # str | Author的邮箱，默认为当前用户的邮箱 (optional)

try:
    # 更新文件
    api_response = api_instance.put_v5_repos_owner_repo_contents_path(owner, repo, path, content, sha, message, access_token=access_token, branch=branch, committer_name=committer_name, committer_email=committer_email, author_name=author_name, author_email=author_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_v5_repos_owner_repo_contents_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **path** | **str**| 文件的路径 | 
 **content** | **str**| 文件内容, 要用 base64 编码 | 
 **sha** | **str**| 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取 | 
 **message** | **str**| 提交信息 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **branch** | **str**| 分支名称。默认为仓库对默认分支 | [optional] 
 **committer_name** | **str**| Committer的名字，默认为当前用户的名字 | [optional] 
 **committer_email** | **str**| Committer的邮箱，默认为当前用户的邮箱 | [optional] 
 **author_name** | **str**| Author的名字，默认为当前用户的名字 | [optional] 
 **author_email** | **str**| Author的邮箱，默认为当前用户的邮箱 | [optional] 

### Return type

[**CommitContent**](CommitContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_keys_enable_id**
> put_v5_repos_owner_repo_keys_enable_id(owner, repo, id, access_token=access_token)

启用仓库公钥

启用仓库公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 启用仓库公钥
    api_instance.put_v5_repos_owner_repo_keys_enable_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_v5_repos_owner_repo_keys_enable_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_reviewer**
> put_v5_repos_owner_repo_reviewer(owner, repo, body)

修改代码审查设置

修改代码审查设置

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.RepositoriesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = gitee.SetRepoReviewer() # SetRepoReviewer | 修改代码审查的信息

try:
    # 修改代码审查设置
    api_instance.put_v5_repos_owner_repo_reviewer(owner, repo, body)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_v5_repos_owner_repo_reviewer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**SetRepoReviewer**](SetRepoReviewer.md)| 修改代码审查的信息 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

