# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    OpenAPI spec version: 6.6.0.20190329.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.authentication_api import AuthenticationApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authentication_access_tokens_post(self):
        """Test case for authentication_access_tokens_post

        Generate an access token for user authentication.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
