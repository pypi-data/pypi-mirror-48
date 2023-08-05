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


class Transaction(object):
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
        'transaction_state': 'str',
        'ipg_transaction_id': 'str',
        'order_id': 'str',
        'transaction_type': 'TransactionType',
        'payment_method_details': 'PaymentMethodDetails',
        'transaction_amount': 'Amount',
        'submission_component': 'str',
        'payer_security_level': 'str',
        'transaction_time': 'int',
        'store_id': 'str',
        'user_id': 'str',
        'processor': 'ProcessorData'
    }

    attribute_map = {
        'transaction_state': 'transactionState',
        'ipg_transaction_id': 'ipgTransactionId',
        'order_id': 'orderId',
        'transaction_type': 'transactionType',
        'payment_method_details': 'paymentMethodDetails',
        'transaction_amount': 'transactionAmount',
        'submission_component': 'submissionComponent',
        'payer_security_level': 'payerSecurityLevel',
        'transaction_time': 'transactionTime',
        'store_id': 'storeId',
        'user_id': 'userId',
        'processor': 'processor'
    }

    def __init__(self, transaction_state=None, ipg_transaction_id=None, order_id=None, transaction_type=None, payment_method_details=None, transaction_amount=None, submission_component=None, payer_security_level=None, transaction_time=None, store_id=None, user_id=None, processor=None):  # noqa: E501
        """Transaction - a model defined in OpenAPI"""  # noqa: E501

        self._transaction_state = None
        self._ipg_transaction_id = None
        self._order_id = None
        self._transaction_type = None
        self._payment_method_details = None
        self._transaction_amount = None
        self._submission_component = None
        self._payer_security_level = None
        self._transaction_time = None
        self._store_id = None
        self._user_id = None
        self._processor = None
        self.discriminator = None

        if transaction_state is not None:
            self.transaction_state = transaction_state
        if ipg_transaction_id is not None:
            self.ipg_transaction_id = ipg_transaction_id
        if order_id is not None:
            self.order_id = order_id
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if payment_method_details is not None:
            self.payment_method_details = payment_method_details
        if transaction_amount is not None:
            self.transaction_amount = transaction_amount
        if submission_component is not None:
            self.submission_component = submission_component
        if payer_security_level is not None:
            self.payer_security_level = payer_security_level
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if store_id is not None:
            self.store_id = store_id
        if user_id is not None:
            self.user_id = user_id
        if processor is not None:
            self.processor = processor

    @property
    def transaction_state(self):
        """Gets the transaction_state of this Transaction.  # noqa: E501

        The state of the transaction.  # noqa: E501

        :return: The transaction_state of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_state

    @transaction_state.setter
    def transaction_state(self, transaction_state):
        """Sets the transaction_state of this Transaction.

        The state of the transaction.  # noqa: E501

        :param transaction_state: The transaction_state of this Transaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTHORIZED", "CAPTURED", "COMPLETED_GET", "DECLINED", "CHECKED", "INITIALIZED", "PENDING_AUTHORIZATION", "PENDING_AUTOVOID", "PENDING_CAPTURE", "PENDING_CREDIT", "PENDING_GIROPAY_INIT", "PENDING_IDEAL_INIT", "PENDING_INIT", "PENDING_READY", "PENDING_RETURN", "PENDING_SETTLEMENT", "PENDING_SOFORT_INIT", "PENDING_VOID", "READY", "SETTLED", "VOIDED", "WAITING", "WAITING_AUTHENTICATION", "WAITING_3D_SECURE", "WAITING_CLICK_AND_BUY", "WAITING_GIROPAY", "WAITING_IDEAL", "WAITING_KLARNA", "WAITING_PAYPAL", "WAITING_PAYPAL_EVENT", "WAITING_PPRO_LONG_WAITING", "WAITING_SOFORT", "WAITING_T_PAY", "WAITING_ALIPAY_PAYSECURE"]  # noqa: E501
        if transaction_state not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_state` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_state, allowed_values)
            )

        self._transaction_state = transaction_state

    @property
    def ipg_transaction_id(self):
        """Gets the ipg_transaction_id of this Transaction.  # noqa: E501

        The transaction ID.  # noqa: E501

        :return: The ipg_transaction_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._ipg_transaction_id

    @ipg_transaction_id.setter
    def ipg_transaction_id(self, ipg_transaction_id):
        """Sets the ipg_transaction_id of this Transaction.

        The transaction ID.  # noqa: E501

        :param ipg_transaction_id: The ipg_transaction_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._ipg_transaction_id = ipg_transaction_id

    @property
    def order_id(self):
        """Gets the order_id of this Transaction.  # noqa: E501

        Client order ID if supplied by client.  # noqa: E501

        :return: The order_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Transaction.

        Client order ID if supplied by client.  # noqa: E501

        :param order_id: The order_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def transaction_type(self):
        """Gets the transaction_type of this Transaction.  # noqa: E501


        :return: The transaction_type of this Transaction.  # noqa: E501
        :rtype: TransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this Transaction.


        :param transaction_type: The transaction_type of this Transaction.  # noqa: E501
        :type: TransactionType
        """

        self._transaction_type = transaction_type

    @property
    def payment_method_details(self):
        """Gets the payment_method_details of this Transaction.  # noqa: E501


        :return: The payment_method_details of this Transaction.  # noqa: E501
        :rtype: PaymentMethodDetails
        """
        return self._payment_method_details

    @payment_method_details.setter
    def payment_method_details(self, payment_method_details):
        """Sets the payment_method_details of this Transaction.


        :param payment_method_details: The payment_method_details of this Transaction.  # noqa: E501
        :type: PaymentMethodDetails
        """

        self._payment_method_details = payment_method_details

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this Transaction.  # noqa: E501


        :return: The transaction_amount of this Transaction.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this Transaction.


        :param transaction_amount: The transaction_amount of this Transaction.  # noqa: E501
        :type: Amount
        """

        self._transaction_amount = transaction_amount

    @property
    def submission_component(self):
        """Gets the submission_component of this Transaction.  # noqa: E501

        The submission component.  # noqa: E501

        :return: The submission_component of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._submission_component

    @submission_component.setter
    def submission_component(self, submission_component):
        """Sets the submission_component of this Transaction.

        The submission component.  # noqa: E501

        :param submission_component: The submission_component of this Transaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["API", "BUS", "CONNECT", "CORE", "EPAS", "MCS", "RESTAPI", "SWITCH", "VT"]  # noqa: E501
        if submission_component not in allowed_values:
            raise ValueError(
                "Invalid value for `submission_component` ({0}), must be one of {1}"  # noqa: E501
                .format(submission_component, allowed_values)
            )

        self._submission_component = submission_component

    @property
    def payer_security_level(self):
        """Gets the payer_security_level of this Transaction.  # noqa: E501

        The payer security level.  # noqa: E501

        :return: The payer_security_level of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._payer_security_level

    @payer_security_level.setter
    def payer_security_level(self, payer_security_level):
        """Sets the payer_security_level of this Transaction.

        The payer security level.  # noqa: E501

        :param payer_security_level: The payer_security_level of this Transaction.  # noqa: E501
        :type: str
        """

        self._payer_security_level = payer_security_level

    @property
    def transaction_time(self):
        """Gets the transaction_time of this Transaction.  # noqa: E501

        The transaction time in seconds since epoch.  # noqa: E501

        :return: The transaction_time of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this Transaction.

        The transaction time in seconds since epoch.  # noqa: E501

        :param transaction_time: The transaction_time of this Transaction.  # noqa: E501
        :type: int
        """

        self._transaction_time = transaction_time

    @property
    def store_id(self):
        """Gets the store_id of this Transaction.  # noqa: E501

        Store ID number.  # noqa: E501

        :return: The store_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this Transaction.

        Store ID number.  # noqa: E501

        :param store_id: The store_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def user_id(self):
        """Gets the user_id of this Transaction.  # noqa: E501

        The user ID.  # noqa: E501

        :return: The user_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Transaction.

        The user ID.  # noqa: E501

        :param user_id: The user_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def processor(self):
        """Gets the processor of this Transaction.  # noqa: E501


        :return: The processor of this Transaction.  # noqa: E501
        :rtype: ProcessorData
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this Transaction.


        :param processor: The processor of this Transaction.  # noqa: E501
        :type: ProcessorData
        """

        self._processor = processor

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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
