import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.endpoints_auth_login200_response import EndpointsAuthLogin200Response  # noqa: E501
from openapi_server.models.endpoints_auth_login_request import EndpointsAuthLoginRequest  # noqa: E501
from openapi_server.models.endpoints_auth_protected200_response import EndpointsAuthProtected200Response  # noqa: E501
from openapi_server import util


def endpoints_auth_login(endpoints_auth_login_request):  # noqa: E501
    """Login a user

     # noqa: E501

    :param endpoints_auth_login_request: 
    :type endpoints_auth_login_request: dict | bytes

    :rtype: Union[EndpointsAuthLogin200Response, Tuple[EndpointsAuthLogin200Response, int], Tuple[EndpointsAuthLogin200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        endpoints_auth_login_request = EndpointsAuthLoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def endpoints_auth_protected():  # noqa: E501
    """Protected endpoint

     # noqa: E501


    :rtype: Union[EndpointsAuthProtected200Response, Tuple[EndpointsAuthProtected200Response, int], Tuple[EndpointsAuthProtected200Response, int, Dict[str, str]]
    """
    return 'do some magic!'
