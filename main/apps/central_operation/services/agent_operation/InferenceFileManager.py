"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config
import io

def download(payload):
    """
    Call agent_operation.InferenceFileManager.download API
    """
    module_name_str = config.AGENT_OPERATION.NAME
    actor_name_str = "InferenceFileManager"
    function_name_str = "download"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    file = io.BytesIO(response.content)
    # file = response.content
    return file

