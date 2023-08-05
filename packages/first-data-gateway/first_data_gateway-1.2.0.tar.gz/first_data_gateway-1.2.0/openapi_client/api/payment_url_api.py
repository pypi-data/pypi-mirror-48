# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    OpenAPI spec version: 6.6.0.20190329.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class PaymentURLApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_payment_url(self, content_type, client_request_id, api_key, timestamp, payment_url_request, **kwargs):  # noqa: E501
        """Create a payment URL.  # noqa: E501

        Use this to generate an embedding payment link.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_url(content_type, client_request_id, api_key, timestamp, payment_url_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: Content type. (required)
        :param str client_request_id: A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. (required)
        :param str api_key: Key given to merchant after boarding associating their requests with the appropriate app in Apigee. (required)
        :param int timestamp: Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). (required)
        :param PaymentUrlRequest payment_url_request: Accepted request type: PaymentUrlRequest. (required)
        :param str message_signature: Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal.
        :param str region: Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing.
        :return: PaymentUrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_payment_url_with_http_info(content_type, client_request_id, api_key, timestamp, payment_url_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_payment_url_with_http_info(content_type, client_request_id, api_key, timestamp, payment_url_request, **kwargs)  # noqa: E501
            return data

    def create_payment_url_with_http_info(self, content_type, client_request_id, api_key, timestamp, payment_url_request, **kwargs):  # noqa: E501
        """Create a payment URL.  # noqa: E501

        Use this to generate an embedding payment link.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_url_with_http_info(content_type, client_request_id, api_key, timestamp, payment_url_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: Content type. (required)
        :param str client_request_id: A client-generated ID for request tracking and signature creation, unique per request.  This is also used for idempotency control. We recommend 128-bit UUID format. (required)
        :param str api_key: Key given to merchant after boarding associating their requests with the appropriate app in Apigee. (required)
        :param int timestamp: Epoch timestamp in milliseconds in the request from a client system. Used for Message Signature generation and time limit (5 mins). (required)
        :param PaymentUrlRequest payment_url_request: Accepted request type: PaymentUrlRequest. (required)
        :param str message_signature: Used to ensure the request has not been tampered with during transmission. The Message-Signature is the Base64 encoded HMAC hash (SHA256 algorithm with the API Secret as the key.) For more information, refer to the supporting documentation on the Developer Portal.
        :param str region: Indicates the region where the client wants the transaction to be processed. This will override the default processing region identified for the client. Available options are argentina, brazil, germany, india and northamerica. Region specific store setup and APIGEE boarding is required in order to use an alternate region for processing.
        :return: PaymentUrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['content_type', 'client_request_id', 'api_key', 'timestamp', 'payment_url_request', 'message_signature', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment_url" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in local_var_params or
                local_var_params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `create_payment_url`")  # noqa: E501
        # verify the required parameter 'client_request_id' is set
        if ('client_request_id' not in local_var_params or
                local_var_params['client_request_id'] is None):
            raise ValueError("Missing the required parameter `client_request_id` when calling `create_payment_url`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in local_var_params or
                local_var_params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `create_payment_url`")  # noqa: E501
        # verify the required parameter 'timestamp' is set
        if ('timestamp' not in local_var_params or
                local_var_params['timestamp'] is None):
            raise ValueError("Missing the required parameter `timestamp` when calling `create_payment_url`")  # noqa: E501
        # verify the required parameter 'payment_url_request' is set
        if ('payment_url_request' not in local_var_params or
                local_var_params['payment_url_request'] is None):
            raise ValueError("Missing the required parameter `payment_url_request` when calling `create_payment_url`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']  # noqa: E501
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']  # noqa: E501
        if 'api_key' in local_var_params:
            header_params['Api-Key'] = local_var_params['api_key']  # noqa: E501
        if 'timestamp' in local_var_params:
            header_params['Timestamp'] = local_var_params['timestamp']  # noqa: E501
        if 'message_signature' in local_var_params:
            header_params['Message-Signature'] = local_var_params['message_signature']  # noqa: E501
        if 'region' in local_var_params:
            header_params['Region'] = local_var_params['region']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_url_request' in local_var_params:
            body_params = local_var_params['payment_url_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/payment-url', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentUrlResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
