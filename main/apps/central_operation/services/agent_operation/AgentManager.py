"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def verify(payload):
    """
    Call agent_operation.AgentManager.verify API
    """
    module_name_str = config.AGENT_OPERATION.NAME
    actor_name_str = "AuthManager"
    function_name_str = "verify"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict

