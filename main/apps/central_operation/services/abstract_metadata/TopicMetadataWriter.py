"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def create(payload):
    """
    Call abstract_metadata.TopicMetadataWriter.create API
    """
    module_name_str = config.ABSTRACT_METADATA.NAME
    actor_name_str = "TopicMetadataWriter"
    function_name_str = "create"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict

def retrieve(payload):
    """
    Call abstract_metadata.TopicMetadataWriter.retrieve API
    """
    module_name_str = config.ABSTRACT_METADATA.NAME
    actor_name_str = "TopicMetadataWriter"
    function_name_str = "retrieve"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict

def delete(payload):
    """
    Call abstract_metadata.TopicMetadataWriter.delete API
    """
    module_name_str = config.ABSTRACT_METADATA.NAME
    actor_name_str = "TopicMetadataWriter"
    function_name_str = "delete"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_str = response_dict["detail"]

    return response_str

def filter_by_agent(payload):
    """
    Call abstract_metadata.TopicMetadataWriter.filter_by_agent API
    """
    module_name_str = config.ABSTRACT_METADATA.NAME
    actor_name_str = "TopicMetadataWriter"
    function_name_str = "filter_by_agent"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict

