"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def subscribe(payload):
    """
    Call central_operation.ModelMetadataWriter.subscribe API
    """
    module_name_str = config.CENTRAL_OPERATION.NAME
    actor_name_str = "TopicSubscriber"
    function_name_str = "subscribe"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["detail"]

    return response_dict

def unsubscribe(payload):
    """
    Call central_operation.ModelMetadataWriter.subscribe API
    """
    module_name_str = config.CENTRAL_OPERATION.NAME
    actor_name_str = "TopicSubscriber"
    function_name_str = "unsubscribe"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["detail"]

    return response_dict
