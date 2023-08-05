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


class Amount(object):
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
        'total': 'float',
        'currency': 'str',
        'components': 'AmountComponents'
    }

    attribute_map = {
        'total': 'total',
        'currency': 'currency',
        'components': 'components'
    }

    def __init__(self, total=None, currency=None, components=None):  # noqa: E501
        """Amount - a model defined in OpenAPI"""  # noqa: E501

        self._total = None
        self._currency = None
        self._components = None
        self.discriminator = None

        self.total = total
        self.currency = currency
        if components is not None:
            self.components = components

    @property
    def total(self):
        """Gets the total of this Amount.  # noqa: E501

        Amount total.  # noqa: E501

        :return: The total of this Amount.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Amount.

        Amount total.  # noqa: E501

        :param total: The total of this Amount.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def currency(self):
        """Gets the currency of this Amount.  # noqa: E501

        ISO 4217 currency code.  # noqa: E501

        :return: The currency of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Amount.

        ISO 4217 currency code.  # noqa: E501

        :param currency: The currency of this Amount.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def components(self):
        """Gets the components of this Amount.  # noqa: E501


        :return: The components of this Amount.  # noqa: E501
        :rtype: AmountComponents
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this Amount.


        :param components: The components of this Amount.  # noqa: E501
        :type: AmountComponents
        """

        self._components = components

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
        if not isinstance(other, Amount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
