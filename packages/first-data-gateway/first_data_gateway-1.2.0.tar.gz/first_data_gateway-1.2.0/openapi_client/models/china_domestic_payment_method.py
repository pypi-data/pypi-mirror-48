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


class ChinaDomesticPaymentMethod(object):
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
        'china_domestic': 'ChinaDomestic',
        'brand': 'str'
    }

    attribute_map = {
        'china_domestic': 'chinaDomestic',
        'brand': 'brand'
    }

    def __init__(self, china_domestic=None, brand=None):  # noqa: E501
        """ChinaDomesticPaymentMethod - a model defined in OpenAPI"""  # noqa: E501

        self._china_domestic = None
        self._brand = None
        self.discriminator = None

        self.china_domestic = china_domestic
        self.brand = brand

    @property
    def china_domestic(self):
        """Gets the china_domestic of this ChinaDomesticPaymentMethod.  # noqa: E501


        :return: The china_domestic of this ChinaDomesticPaymentMethod.  # noqa: E501
        :rtype: ChinaDomestic
        """
        return self._china_domestic

    @china_domestic.setter
    def china_domestic(self, china_domestic):
        """Sets the china_domestic of this ChinaDomesticPaymentMethod.


        :param china_domestic: The china_domestic of this ChinaDomesticPaymentMethod.  # noqa: E501
        :type: ChinaDomestic
        """
        if china_domestic is None:
            raise ValueError("Invalid value for `china_domestic`, must not be `None`")  # noqa: E501

        self._china_domestic = china_domestic

    @property
    def brand(self):
        """Gets the brand of this ChinaDomesticPaymentMethod.  # noqa: E501


        :return: The brand of this ChinaDomesticPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this ChinaDomesticPaymentMethod.


        :param brand: The brand of this ChinaDomesticPaymentMethod.  # noqa: E501
        :type: str
        """
        if brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501
        allowed_values = ["ALIPAY_DOMESTIC", "CUP_DOMESTIC", "WECHAT_DOMESTIC"]  # noqa: E501
        if brand not in allowed_values:
            raise ValueError(
                "Invalid value for `brand` ({0}), must be one of {1}"  # noqa: E501
                .format(brand, allowed_values)
            )

        self._brand = brand

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
        if not isinstance(other, ChinaDomesticPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
