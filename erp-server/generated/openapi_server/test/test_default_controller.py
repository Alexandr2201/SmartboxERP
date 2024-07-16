import unittest

from flask import json

from openapi_server.models.login_post200_response import LoginPost200Response  # noqa: E501
from openapi_server.models.login_post_request import LoginPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_login_post(self):
        """Test case for login_post

        Login user
        """
        login_post_request = openapi_server.LoginPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/login',
            method='POST',
            headers=headers,
            data=json.dumps(login_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
