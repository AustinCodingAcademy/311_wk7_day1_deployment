"""Generated client library for remotebuildexecution version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.remotebuildexecution.v1alpha import remotebuildexecution_v1alpha_messages as messages


class RemotebuildexecutionV1alpha(base_api.BaseApiClient):
  """Generated client library for service remotebuildexecution version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://admin-remotebuildexecution.googleapis.com/'

  _PACKAGE = u'remotebuildexecution'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'RemotebuildexecutionV1alpha'
  _URL_VERSION = u'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new remotebuildexecution handle."""
    url = url or self.BASE_URL
    super(RemotebuildexecutionV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_instances_workerpools = self.ProjectsInstancesWorkerpoolsService(self)
    self.projects_instances = self.ProjectsInstancesService(self)
    self.projects_operations = self.ProjectsOperationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsInstancesWorkerpoolsService(base_api.BaseApiService):
    """Service class for the projects_instances_workerpools resource."""

    _NAME = u'projects_instances_workerpools'

    def __init__(self, client):
      super(RemotebuildexecutionV1alpha.ProjectsInstancesWorkerpoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new worker pool with a specified size and configuration.
Returns a long running operation which contains a worker pool on
completion. While the long running operation is in progress, any call to
`GetWorkerPool` returns a worker pool in state `CREATING`.

      Args:
        request: (GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools',
        http_method=u'POST',
        method_id=u'remotebuildexecution.projects.instances.workerpools.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha/{+parent}/workerpools',
        request_field='<request>',
        request_type_name=u'GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the specified worker pool.
Returns a long running operation, which contains a `google.protobuf.Empty`
response on completion.
While the long running operation is in progress, any call to
`GetWorkerPool` returns a worker pool in state `DELETING`.

      Args:
        request: (RemotebuildexecutionProjectsInstancesWorkerpoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools/{workerpoolsId}',
        http_method=u'DELETE',
        method_id=u'remotebuildexecution.projects.instances.workerpools.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'RemotebuildexecutionProjectsInstancesWorkerpoolsDeleteRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns the specified worker pool.

      Args:
        request: (RemotebuildexecutionProjectsInstancesWorkerpoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools/{workerpoolsId}',
        http_method=u'GET',
        method_id=u'remotebuildexecution.projects.instances.workerpools.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'RemotebuildexecutionProjectsInstancesWorkerpoolsGetRequest',
        response_type_name=u'GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists worker pools in an instance.

      Args:
        request: (RemotebuildexecutionProjectsInstancesWorkerpoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools',
        http_method=u'GET',
        method_id=u'remotebuildexecution.projects.instances.workerpools.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter'],
        relative_path=u'v1alpha/{+parent}/workerpools',
        request_field='',
        request_type_name=u'RemotebuildexecutionProjectsInstancesWorkerpoolsListRequest',
        response_type_name=u'GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an existing worker pool with a specified size and/or configuration.
Returns a long running operation, which contains a worker pool on
completion. While the long running operation is in progress, any call to
`GetWorkerPool` returns a worker pool in state `UPDATING`.

      Args:
        request: (RemotebuildexecutionProjectsInstancesWorkerpoolsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools/{workerpoolsId}',
        http_method=u'PATCH',
        method_id=u'remotebuildexecution.projects.instances.workerpools.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field=u'googleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest',
        request_type_name=u'RemotebuildexecutionProjectsInstancesWorkerpoolsPatchRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsInstancesService(base_api.BaseApiService):
    """Service class for the projects_instances resource."""

    _NAME = u'projects_instances'

    def __init__(self, client):
      super(RemotebuildexecutionV1alpha.ProjectsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new instance in the specified region.
Returns a long running operation which contains an instance on completion.
While the long running operation is in progress, any call to `GetInstance`
returns an instance in state `CREATING`.

      Args:
        request: (GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances',
        http_method=u'POST',
        method_id=u'remotebuildexecution.projects.instances.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha/{+parent}/instances',
        request_field='<request>',
        request_type_name=u'GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the specified instance.
Returns a long running operation which contains a `google.protobuf.Empty`
response on completion.
Deleting an instance with worker pools in it will delete these worker
pools.

      Args:
        request: (RemotebuildexecutionProjectsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances/{instancesId}',
        http_method=u'DELETE',
        method_id=u'remotebuildexecution.projects.instances.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'RemotebuildexecutionProjectsInstancesDeleteRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns the specified instance.

      Args:
        request: (RemotebuildexecutionProjectsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances/{instancesId}',
        http_method=u'GET',
        method_id=u'remotebuildexecution.projects.instances.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'RemotebuildexecutionProjectsInstancesGetRequest',
        response_type_name=u'GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists instances in a project.

      Args:
        request: (RemotebuildexecutionProjectsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/instances',
        http_method=u'GET',
        method_id=u'remotebuildexecution.projects.instances.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha/{+parent}/instances',
        request_field='',
        request_type_name=u'RemotebuildexecutionProjectsInstancesListRequest',
        response_type_name=u'GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse',
        supports_download=False,
    )

  class ProjectsOperationsService(base_api.BaseApiService):
    """Service class for the projects_operations resource."""

    _NAME = u'projects_operations'

    def __init__(self, client):
      super(RemotebuildexecutionV1alpha.ProjectsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (RemotebuildexecutionProjectsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/projects/{projectsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'remotebuildexecution.projects.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'RemotebuildexecutionProjectsOperationsGetRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(RemotebuildexecutionV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
