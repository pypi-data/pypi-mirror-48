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


class PaymentMethodType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ALIPAY = "ALIPAY"
    ALIPAY_PAYSECURE_US = "ALIPAY_PAYSECURE_US"
    ALIPAY_DOMESTIC = "ALIPAY_DOMESTIC"
    APM = "APM"
    CUP_DOMESTIC = "CUP_DOMESTIC"
    DEBITDE = "DEBITDE"
    EMI = "EMI"
    GIROPAY = "GIROPAY"
    IDEAL = "IDEAL"
    INDIAWALLET = "INDIAWALLET"
    KLARNA = "KLARNA"
    NETBANKING = "NETBANKING"
    PAYMENT_CARD = "PAYMENT_CARD"
    PAYMENT_TOKEN = "PAYMENT_TOKEN"
    PAYPAL = "PAYPAL"
    SEPA = "SEPA"
    SOFORT = "SOFORT"
    WALLET = "WALLET"
    WECHAT_DOMESTIC = "WECHAT_DOMESTIC"

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """PaymentMethodType - a model defined in OpenAPI"""  # noqa: E501
        self.discriminator = None

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
        if not isinstance(other, PaymentMethodType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
