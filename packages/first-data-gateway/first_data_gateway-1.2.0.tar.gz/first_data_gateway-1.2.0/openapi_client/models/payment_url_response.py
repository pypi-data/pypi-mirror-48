# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.6.0.20190329.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentUrlResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'client_request_id': 'str',
        'api_trace_id': 'str',
        'response_type': 'ResponseType',
        'request_status': 'str',
        'order_id': 'str',
        'payment_url': 'str',
        'transaction_id': 'str'
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',
        'api_trace_id': 'apiTraceId',
        'response_type': 'responseType',
        'request_status': 'requestStatus',
        'order_id': 'orderId',
        'payment_url': 'paymentUrl',
        'transaction_id': 'transactionId'
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, request_status=None, order_id=None, payment_url=None, transaction_id=None):  # noqa: E501
        """PaymentUrlResponse - a model defined in OpenAPI"""  # noqa: E501

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._request_status = None
        self._order_id = None
        self._payment_url = None
        self._transaction_id = None
        self.discriminator = None

        if client_request_id is not None:
            self.client_request_id = client_request_id
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id
        if response_type is not None:
            self.response_type = response_type
        if request_status is not None:
            self.request_status = request_status
        if order_id is not None:
            self.order_id = order_id
        if payment_url is not None:
            self.payment_url = payment_url
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def client_request_id(self):
        """Gets the client_request_id of this PaymentUrlResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this PaymentUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this PaymentUrlResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this PaymentUrlResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this PaymentUrlResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this PaymentUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(self, api_trace_id):
        """Sets the api_trace_id of this PaymentUrlResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this PaymentUrlResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = api_trace_id

    @property
    def response_type(self):
        """Gets the response_type of this PaymentUrlResponse.  # noqa: E501


        :return: The response_type of this PaymentUrlResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this PaymentUrlResponse.


        :param response_type: The response_type of this PaymentUrlResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = response_type

    @property
    def request_status(self):
        """Gets the request_status of this PaymentUrlResponse.  # noqa: E501

        Request status. If it is anything other than 'SUCCESS', please refer to 400s HTTP error codes or decline. See Error object for details.  # noqa: E501

        :return: The request_status of this PaymentUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_status

    @request_status.setter
    def request_status(self, request_status):
        """Sets the request_status of this PaymentUrlResponse.

        Request status. If it is anything other than 'SUCCESS', please refer to 400s HTTP error codes or decline. See Error object for details.  # noqa: E501

        :param request_status: The request_status of this PaymentUrlResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "VALIDATION_FAILED", "PROCESSING_FAILED", "FAILURE"]  # noqa: E501
        if request_status not in allowed_values:
            raise ValueError(
                "Invalid value for `request_status` ({0}), must be one of {1}"  # noqa: E501
                .format(request_status, allowed_values)
            )

        self._request_status = request_status

    @property
    def order_id(self):
        """Gets the order_id of this PaymentUrlResponse.  # noqa: E501

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :return: The order_id of this PaymentUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PaymentUrlResponse.

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :param order_id: The order_id of this PaymentUrlResponse.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def payment_url(self):
        """Gets the payment_url of this PaymentUrlResponse.  # noqa: E501

        URL for embedded payment link.  # noqa: E501

        :return: The payment_url of this PaymentUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_url

    @payment_url.setter
    def payment_url(self, payment_url):
        """Sets the payment_url of this PaymentUrlResponse.

        URL for embedded payment link.  # noqa: E501

        :param payment_url: The payment_url of this PaymentUrlResponse.  # noqa: E501
        :type: str
        """

        self._payment_url = payment_url

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PaymentUrlResponse.  # noqa: E501

        ID code from the transaction.  # noqa: E501

        :return: The transaction_id of this PaymentUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PaymentUrlResponse.

        ID code from the transaction.  # noqa: E501

        :param transaction_id: The transaction_id of this PaymentUrlResponse.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
