"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def create(payload):
    """
    Call entrypoint.ABMAccountManger.create API
    """
    module_name_str = config.ENTRYPOINT.NAME
    actor_name_str = "ABMAccountManger"
    function_name_str = "create"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)
    print("response", response)
    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict
