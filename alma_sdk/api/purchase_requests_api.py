# coding: utf-8

"""
    Ex Libris APIs

    For more information on how to use these APIs, including how to create an API key required for authentication, see [Alma REST APIs](https://developers.exlibrisgroup.com/alma/apis).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from alma_sdk.api_client import ApiClient


class PurchaseRequestsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deletealmawsv1usersuser_idpurchase_requestspurchase_request_id(self, user_id, purchase_request_id, **kwargs):  # noqa: E501
        """Delete user's purchase request.  # noqa: E501

        This Web service deletes a user's purchase request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletealmawsv1usersuser_idpurchase_requestspurchase_request_id(user_id, purchase_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str purchase_request_id: The identifier of the purchase request. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletealmawsv1usersuser_idpurchase_requestspurchase_request_id_with_http_info(user_id, purchase_request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.deletealmawsv1usersuser_idpurchase_requestspurchase_request_id_with_http_info(user_id, purchase_request_id, **kwargs)  # noqa: E501
            return data

    def deletealmawsv1usersuser_idpurchase_requestspurchase_request_id_with_http_info(self, user_id, purchase_request_id, **kwargs):  # noqa: E501
        """Delete user's purchase request.  # noqa: E501

        This Web service deletes a user's purchase request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletealmawsv1usersuser_idpurchase_requestspurchase_request_id_with_http_info(user_id, purchase_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str purchase_request_id: The identifier of the purchase request. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'purchase_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletealmawsv1usersuser_idpurchase_requestspurchase_request_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `deletealmawsv1usersuser_idpurchase_requestspurchase_request_id`")  # noqa: E501
        # verify the required parameter 'purchase_request_id' is set
        if ('purchase_request_id' not in params or
                params['purchase_request_id'] is None):
            raise ValueError("Missing the required parameter `purchase_request_id` when calling `deletealmawsv1usersuser_idpurchase_requestspurchase_request_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501
        if 'purchase_request_id' in params:
            path_params['purchase_request_id'] = params['purchase_request_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/almaws/v1/users/{user_id}/purchase-requests/{purchase_request_id}', 'DELETE',
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

    def getalmawsv1usersuser_idpurchase_requests(self, user_id, user_id_type, **kwargs):  # noqa: E501
        """Retrieve user's purchase requests.  # noqa: E501

        This Web service retrieves a user's purchase requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getalmawsv1usersuser_idpurchase_requests(user_id, user_id_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table. (required)
        :param int limit: Limits the number of results. Optional. Valid values are 0-100. Default value: 10.
        :param int offset: Offset of the results returned. Optional.Default value: 0, which means that the first results will be returned. 
        :param str status: For filtering based on the purchase request's status. Optional. Possible values:  INREVIEW, APPROVED, REJECTED, DEFERRED. Default is no status.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getalmawsv1usersuser_idpurchase_requests_with_http_info(user_id, user_id_type, **kwargs)  # noqa: E501
        else:
            (data) = self.getalmawsv1usersuser_idpurchase_requests_with_http_info(user_id, user_id_type, **kwargs)  # noqa: E501
            return data

    def getalmawsv1usersuser_idpurchase_requests_with_http_info(self, user_id, user_id_type, **kwargs):  # noqa: E501
        """Retrieve user's purchase requests.  # noqa: E501

        This Web service retrieves a user's purchase requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getalmawsv1usersuser_idpurchase_requests_with_http_info(user_id, user_id_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table. (required)
        :param int limit: Limits the number of results. Optional. Valid values are 0-100. Default value: 10.
        :param int offset: Offset of the results returned. Optional.Default value: 0, which means that the first results will be returned. 
        :param str status: For filtering based on the purchase request's status. Optional. Possible values:  INREVIEW, APPROVED, REJECTED, DEFERRED. Default is no status.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'user_id_type', 'limit', 'offset', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getalmawsv1usersuser_idpurchase_requests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `getalmawsv1usersuser_idpurchase_requests`")  # noqa: E501
        # verify the required parameter 'user_id_type' is set
        if ('user_id_type' not in params or
                params['user_id_type'] is None):
            raise ValueError("Missing the required parameter `user_id_type` when calling `getalmawsv1usersuser_idpurchase_requests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'user_id_type' in params:
            query_params.append(('user_id_type', params['user_id_type']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/almaws/v1/users/{user_id}/purchase-requests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getalmawsv1usersuser_idpurchase_requestspurchase_request_id(self, user_id, purchase_request_id, user_id_type, **kwargs):  # noqa: E501
        """Retrieve user's purchase request.  # noqa: E501

        This Web service retrieves a user's purchase request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getalmawsv1usersuser_idpurchase_requestspurchase_request_id(user_id, purchase_request_id, user_id_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str purchase_request_id: The identifier of the purchase request. (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getalmawsv1usersuser_idpurchase_requestspurchase_request_id_with_http_info(user_id, purchase_request_id, user_id_type, **kwargs)  # noqa: E501
        else:
            (data) = self.getalmawsv1usersuser_idpurchase_requestspurchase_request_id_with_http_info(user_id, purchase_request_id, user_id_type, **kwargs)  # noqa: E501
            return data

    def getalmawsv1usersuser_idpurchase_requestspurchase_request_id_with_http_info(self, user_id, purchase_request_id, user_id_type, **kwargs):  # noqa: E501
        """Retrieve user's purchase request.  # noqa: E501

        This Web service retrieves a user's purchase request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getalmawsv1usersuser_idpurchase_requestspurchase_request_id_with_http_info(user_id, purchase_request_id, user_id_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str purchase_request_id: The identifier of the purchase request. (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'purchase_request_id', 'user_id_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getalmawsv1usersuser_idpurchase_requestspurchase_request_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `getalmawsv1usersuser_idpurchase_requestspurchase_request_id`")  # noqa: E501
        # verify the required parameter 'purchase_request_id' is set
        if ('purchase_request_id' not in params or
                params['purchase_request_id'] is None):
            raise ValueError("Missing the required parameter `purchase_request_id` when calling `getalmawsv1usersuser_idpurchase_requestspurchase_request_id`")  # noqa: E501
        # verify the required parameter 'user_id_type' is set
        if ('user_id_type' not in params or
                params['user_id_type'] is None):
            raise ValueError("Missing the required parameter `user_id_type` when calling `getalmawsv1usersuser_idpurchase_requestspurchase_request_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501
        if 'purchase_request_id' in params:
            path_params['purchase_request_id'] = params['purchase_request_id']  # noqa: E501

        query_params = []
        if 'user_id_type' in params:
            query_params.append(('user_id_type', params['user_id_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/almaws/v1/users/{user_id}/purchase-requests/{purchase_request_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def postalmawsv1usersuser_idpurchase_requests(self, body, user_id_type, user_id, **kwargs):  # noqa: E501
        """Create Purchase Request  # noqa: E501

        This API creates a new purchase request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postalmawsv1usersuser_idpurchase_requests(body, user_id_type, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: This method takes a Purchase Request object. See [here](/alma/apis/docs/xsd/rest_purchase_request.xsd?tags=POST) (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table. (required)
        :param str user_id: A unique identifier for the user (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postalmawsv1usersuser_idpurchase_requests_with_http_info(body, user_id_type, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.postalmawsv1usersuser_idpurchase_requests_with_http_info(body, user_id_type, user_id, **kwargs)  # noqa: E501
            return data

    def postalmawsv1usersuser_idpurchase_requests_with_http_info(self, body, user_id_type, user_id, **kwargs):  # noqa: E501
        """Create Purchase Request  # noqa: E501

        This API creates a new purchase request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postalmawsv1usersuser_idpurchase_requests_with_http_info(body, user_id_type, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: This method takes a Purchase Request object. See [here](/alma/apis/docs/xsd/rest_purchase_request.xsd?tags=POST) (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table. (required)
        :param str user_id: A unique identifier for the user (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'user_id_type', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postalmawsv1usersuser_idpurchase_requests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postalmawsv1usersuser_idpurchase_requests`")  # noqa: E501
        # verify the required parameter 'user_id_type' is set
        if ('user_id_type' not in params or
                params['user_id_type'] is None):
            raise ValueError("Missing the required parameter `user_id_type` when calling `postalmawsv1usersuser_idpurchase_requests`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `postalmawsv1usersuser_idpurchase_requests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'user_id_type' in params:
            query_params.append(('user_id_type', params['user_id_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/almaws/v1/users/{user_id}/purchase-requests', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
