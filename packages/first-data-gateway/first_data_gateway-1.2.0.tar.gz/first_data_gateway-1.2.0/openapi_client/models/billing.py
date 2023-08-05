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


class Billing(object):
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
        'name': 'str',
        'customer_id': 'str',
        'birth_date': 'date',
        'contact': 'Contact',
        'address': 'Address'
    }

    attribute_map = {
        'name': 'name',
        'customer_id': 'customerId',
        'birth_date': 'birthDate',
        'contact': 'contact',
        'address': 'address'
    }

    def __init__(self, name=None, customer_id=None, birth_date=None, contact=None, address=None):  # noqa: E501
        """Billing - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._customer_id = None
        self._birth_date = None
        self._contact = None
        self._address = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if customer_id is not None:
            self.customer_id = customer_id
        if birth_date is not None:
            self.birth_date = birth_date
        if contact is not None:
            self.contact = contact
        if address is not None:
            self.address = address

    @property
    def name(self):
        """Gets the name of this Billing.  # noqa: E501

        Billing name.  # noqa: E501

        :return: The name of this Billing.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Billing.

        Billing name.  # noqa: E501

        :param name: The name of this Billing.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 96:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `96`")  # noqa: E501

        self._name = name

    @property
    def customer_id(self):
        """Gets the customer_id of this Billing.  # noqa: E501

        Customer ID for billing purpose.  # noqa: E501

        :return: The customer_id of this Billing.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Billing.

        Customer ID for billing purpose.  # noqa: E501

        :param customer_id: The customer_id of this Billing.  # noqa: E501
        :type: str
        """
        if customer_id is not None and len(customer_id) > 32:
            raise ValueError("Invalid value for `customer_id`, length must be less than or equal to `32`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def birth_date(self):
        """Gets the birth_date of this Billing.  # noqa: E501

        Customer birth date.  # noqa: E501

        :return: The birth_date of this Billing.  # noqa: E501
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this Billing.

        Customer birth date.  # noqa: E501

        :param birth_date: The birth_date of this Billing.  # noqa: E501
        :type: date
        """

        self._birth_date = birth_date

    @property
    def contact(self):
        """Gets the contact of this Billing.  # noqa: E501


        :return: The contact of this Billing.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Billing.


        :param contact: The contact of this Billing.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def address(self):
        """Gets the address of this Billing.  # noqa: E501


        :return: The address of this Billing.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Billing.


        :param address: The address of this Billing.  # noqa: E501
        :type: Address
        """

        self._address = address

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
        if not isinstance(other, Billing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
