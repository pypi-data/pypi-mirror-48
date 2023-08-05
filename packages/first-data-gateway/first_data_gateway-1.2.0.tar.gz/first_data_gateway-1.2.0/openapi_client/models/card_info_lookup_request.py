# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    OpenAPI spec version: 6.6.0.20190329.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CardInfoLookupRequest(object):
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
        'store_id': 'str',
        'payment_card': 'PaymentCard'
    }

    attribute_map = {
        'store_id': 'storeId',
        'payment_card': 'paymentCard'
    }

    def __init__(self, store_id=None, payment_card=None):  # noqa: E501
        """CardInfoLookupRequest - a model defined in OpenAPI"""  # noqa: E501

        self._store_id = None
        self._payment_card = None
        self.discriminator = None

        if store_id is not None:
            self.store_id = store_id
        self.payment_card = payment_card

    @property
    def store_id(self):
        """Gets the store_id of this CardInfoLookupRequest.  # noqa: E501

        An optional outlet id for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The store_id of this CardInfoLookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this CardInfoLookupRequest.

        An optional outlet id for clients that support multiple stores in the same developer app.  # noqa: E501

        :param store_id: The store_id of this CardInfoLookupRequest.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def payment_card(self):
        """Gets the payment_card of this CardInfoLookupRequest.  # noqa: E501


        :return: The payment_card of this CardInfoLookupRequest.  # noqa: E501
        :rtype: PaymentCard
        """
        return self._payment_card

    @payment_card.setter
    def payment_card(self, payment_card):
        """Sets the payment_card of this CardInfoLookupRequest.


        :param payment_card: The payment_card of this CardInfoLookupRequest.  # noqa: E501
        :type: PaymentCard
        """
        if payment_card is None:
            raise ValueError("Invalid value for `payment_card`, must not be `None`")  # noqa: E501

        self._payment_card = payment_card

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
        if not isinstance(other, CardInfoLookupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
