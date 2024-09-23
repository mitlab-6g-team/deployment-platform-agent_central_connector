"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def check(payload):
    """
    Call file_operation.FileManager.check API
    """
    module_name_str = config.FILE_OPERATION.NAME
    actor_name_str = "FileManager"
    function_name_str = "check"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_bol = response_dict["data"]

    return response_bol

def save(payload):
    """
    Call file_operation.FileManager.save API
    """
    module_name_str = config.FILE_OPERATION.NAME
    actor_name_str = "FileManager"
    function_name_str = "save"
    
    response = request.for_file(module_name_str, actor_name_str, function_name_str, payload)
    response_dict = response.json()
    response_str = response_dict["detail"]

    return response_str
