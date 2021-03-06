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


class LoansApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def getalmawsv1usersuser_idloans(self, user_id, **kwargs):  # noqa: E501
        """Retrieve user loans  # noqa: E501

        This Web service retrieves a list of active loans for a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getalmawsv1usersuser_idloans(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table.
        :param int limit: Limits the number of results. Optional. Valid values are 0-100. Default value: 10.
        :param int offset: Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned. 
        :param str order_by: A few sort options are available (only one can be sent): loan_date, due_date, barcode, title and author. A secondary sort key, id, is added to the single sort option chosen. Default sorting is by id.
        :param str direction: Sorting direction: ASC/DESC. Default: ASC.
        :param str expand: Comma separated list of values for expansion of results. Possible values: 'renewable'
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getalmawsv1usersuser_idloans_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getalmawsv1usersuser_idloans_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def getalmawsv1usersuser_idloans_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Retrieve user loans  # noqa: E501

        This Web service retrieves a list of active loans for a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getalmawsv1usersuser_idloans_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table.
        :param int limit: Limits the number of results. Optional. Valid values are 0-100. Default value: 10.
        :param int offset: Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned. 
        :param str order_by: A few sort options are available (only one can be sent): loan_date, due_date, barcode, title and author. A secondary sort key, id, is added to the single sort option chosen. Default sorting is by id.
        :param str direction: Sorting direction: ASC/DESC. Default: ASC.
        :param str expand: Comma separated list of values for expansion of results. Possible values: 'renewable'
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'user_id_type', 'limit', 'offset', 'order_by', 'direction', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getalmawsv1usersuser_idloans" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `getalmawsv1usersuser_idloans`")  # noqa: E501

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
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'direction' in params:
            query_params.append(('direction', params['direction']))  # noqa: E501
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

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
            '/almaws/v1/users/{user_id}/loans', 'GET',
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

    def getalmawsv1usersuser_idloansloan_id(self, user_id, loan_id, **kwargs):  # noqa: E501
        """Loan by user id and loan id  # noqa: E501

        This Web service retrieves the user loan for a particular user id and loan id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getalmawsv1usersuser_idloansloan_id(user_id, loan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str loan_id: A unique identifier for the loan (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getalmawsv1usersuser_idloansloan_id_with_http_info(user_id, loan_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getalmawsv1usersuser_idloansloan_id_with_http_info(user_id, loan_id, **kwargs)  # noqa: E501
            return data

    def getalmawsv1usersuser_idloansloan_id_with_http_info(self, user_id, loan_id, **kwargs):  # noqa: E501
        """Loan by user id and loan id  # noqa: E501

        This Web service retrieves the user loan for a particular user id and loan id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getalmawsv1usersuser_idloansloan_id_with_http_info(user_id, loan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str loan_id: A unique identifier for the loan (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'loan_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getalmawsv1usersuser_idloansloan_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `getalmawsv1usersuser_idloansloan_id`")  # noqa: E501
        # verify the required parameter 'loan_id' is set
        if ('loan_id' not in params or
                params['loan_id'] is None):
            raise ValueError("Missing the required parameter `loan_id` when calling `getalmawsv1usersuser_idloansloan_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501
        if 'loan_id' in params:
            path_params['loan_id'] = params['loan_id']  # noqa: E501

        query_params = []

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
            '/almaws/v1/users/{user_id}/loans/{loan_id}', 'GET',
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

    def postalmawsv1usersuser_idloans(self, body, item_pid, item_barcode, user_id, **kwargs):  # noqa: E501
        """Create user loan  # noqa: E501

        This Web service loans an item to a user. The loan will be created according to the library's policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postalmawsv1usersuser_idloans(body, item_pid, item_barcode, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: This method takes a Loan object. See [here](/alma/apis/docs/xsd/rest_item_loan.xsd?tags=POST) (required)
        :param str item_pid: The Item ID. This parameter or the item_barcode parameter must be supplied. (required)
        :param str item_barcode: The Item barcode. This parameter or the item_pid parameter must be supplied. (required)
        :param str user_id: A unique identifier for the user (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postalmawsv1usersuser_idloans_with_http_info(body, item_pid, item_barcode, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.postalmawsv1usersuser_idloans_with_http_info(body, item_pid, item_barcode, user_id, **kwargs)  # noqa: E501
            return data

    def postalmawsv1usersuser_idloans_with_http_info(self, body, item_pid, item_barcode, user_id, **kwargs):  # noqa: E501
        """Create user loan  # noqa: E501

        This Web service loans an item to a user. The loan will be created according to the library's policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postalmawsv1usersuser_idloans_with_http_info(body, item_pid, item_barcode, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: This method takes a Loan object. See [here](/alma/apis/docs/xsd/rest_item_loan.xsd?tags=POST) (required)
        :param str item_pid: The Item ID. This parameter or the item_barcode parameter must be supplied. (required)
        :param str item_barcode: The Item barcode. This parameter or the item_pid parameter must be supplied. (required)
        :param str user_id: A unique identifier for the user (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'item_pid', 'item_barcode', 'user_id', 'user_id_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postalmawsv1usersuser_idloans" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postalmawsv1usersuser_idloans`")  # noqa: E501
        # verify the required parameter 'item_pid' is set
        if ('item_pid' not in params or
                params['item_pid'] is None):
            raise ValueError("Missing the required parameter `item_pid` when calling `postalmawsv1usersuser_idloans`")  # noqa: E501
        # verify the required parameter 'item_barcode' is set
        if ('item_barcode' not in params or
                params['item_barcode'] is None):
            raise ValueError("Missing the required parameter `item_barcode` when calling `postalmawsv1usersuser_idloans`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `postalmawsv1usersuser_idloans`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'item_pid' in params:
            query_params.append(('item_pid', params['item_pid']))  # noqa: E501
        if 'user_id_type' in params:
            query_params.append(('user_id_type', params['user_id_type']))  # noqa: E501
        if 'item_barcode' in params:
            query_params.append(('item_barcode', params['item_barcode']))  # noqa: E501

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
            '/almaws/v1/users/{user_id}/loans', 'POST',
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

    def postalmawsv1usersuser_idloansloan_id(self, user_id, loan_id, op, **kwargs):  # noqa: E501
        """Renew loan  # noqa: E501

        This Web service renews a loan.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postalmawsv1usersuser_idloansloan_id(user_id, loan_id, op, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str loan_id: A unique identifier for the loan (required)
        :param str op: Operation. Currently only op=renew is supported (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postalmawsv1usersuser_idloansloan_id_with_http_info(user_id, loan_id, op, **kwargs)  # noqa: E501
        else:
            (data) = self.postalmawsv1usersuser_idloansloan_id_with_http_info(user_id, loan_id, op, **kwargs)  # noqa: E501
            return data

    def postalmawsv1usersuser_idloansloan_id_with_http_info(self, user_id, loan_id, op, **kwargs):  # noqa: E501
        """Renew loan  # noqa: E501

        This Web service renews a loan.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postalmawsv1usersuser_idloansloan_id_with_http_info(user_id, loan_id, op, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: A unique identifier for the user (required)
        :param str loan_id: A unique identifier for the loan (required)
        :param str op: Operation. Currently only op=renew is supported (required)
        :param str user_id_type: The type of identifier that is being searched. Optional. If this is not provided, all unique identifier types are used. The values that can be used are any of the values in the User Identifier Type code table.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'loan_id', 'op', 'user_id_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postalmawsv1usersuser_idloansloan_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `postalmawsv1usersuser_idloansloan_id`")  # noqa: E501
        # verify the required parameter 'loan_id' is set
        if ('loan_id' not in params or
                params['loan_id'] is None):
            raise ValueError("Missing the required parameter `loan_id` when calling `postalmawsv1usersuser_idloansloan_id`")  # noqa: E501
        # verify the required parameter 'op' is set
        if ('op' not in params or
                params['op'] is None):
            raise ValueError("Missing the required parameter `op` when calling `postalmawsv1usersuser_idloansloan_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501
        if 'loan_id' in params:
            path_params['loan_id'] = params['loan_id']  # noqa: E501

        query_params = []
        if 'user_id_type' in params:
            query_params.append(('user_id_type', params['user_id_type']))  # noqa: E501
        if 'op' in params:
            query_params.append(('op', params['op']))  # noqa: E501

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
            '/almaws/v1/users/{user_id}/loans/{loan_id}', 'POST',
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

    def putalmawsv1usersuser_idloansloan_id(self, body, user_id, loan_id, **kwargs):  # noqa: E501
        """Change loan due date  # noqa: E501

        This Web service changes a loan due date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putalmawsv1usersuser_idloansloan_id(body, user_id, loan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: This method takes an item loan object See [here](/alma/apis/docs/xsd/rest_item_loan.xsd?tags=PUT) (required)
        :param str user_id: A unique identifier for the user (required)
        :param str loan_id: A unique identifier for the loan (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.putalmawsv1usersuser_idloansloan_id_with_http_info(body, user_id, loan_id, **kwargs)  # noqa: E501
        else:
            (data) = self.putalmawsv1usersuser_idloansloan_id_with_http_info(body, user_id, loan_id, **kwargs)  # noqa: E501
            return data

    def putalmawsv1usersuser_idloansloan_id_with_http_info(self, body, user_id, loan_id, **kwargs):  # noqa: E501
        """Change loan due date  # noqa: E501

        This Web service changes a loan due date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putalmawsv1usersuser_idloansloan_id_with_http_info(body, user_id, loan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: This method takes an item loan object See [here](/alma/apis/docs/xsd/rest_item_loan.xsd?tags=PUT) (required)
        :param str user_id: A unique identifier for the user (required)
        :param str loan_id: A unique identifier for the loan (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'user_id', 'loan_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putalmawsv1usersuser_idloansloan_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `putalmawsv1usersuser_idloansloan_id`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `putalmawsv1usersuser_idloansloan_id`")  # noqa: E501
        # verify the required parameter 'loan_id' is set
        if ('loan_id' not in params or
                params['loan_id'] is None):
            raise ValueError("Missing the required parameter `loan_id` when calling `putalmawsv1usersuser_idloansloan_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501
        if 'loan_id' in params:
            path_params['loan_id'] = params['loan_id']  # noqa: E501

        query_params = []

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
            '/almaws/v1/users/{user_id}/loans/{loan_id}', 'PUT',
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
