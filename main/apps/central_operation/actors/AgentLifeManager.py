from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.utils.packet import unpacking
from django.http import JsonResponse
from main.apps.central_operation.services.agent_operation import AgentManager
from main.apps.central_operation.services.abstract_metadata import ApplicationMetadataWriter
from main.apps.central_operation.services.file_metadata import ModelMetadataWriter
from main.apps.central_operation.services.central_operation import TopicSubscriber
from main.apps.central_operation.services.entrypoint import ABMAccountManger

@log_trigger("INFO")
@require_POST
def init(request):
    data_dict = unpacking(request)

    agent_uid_str = data_dict['agent_uid']
    agent_activation_token_str = data_dict['agent_activation_token']
    payload_dict = {
        "agent_uid": agent_uid_str,
        "agent_activation_token": agent_activation_token_str
    }
    metadatas_dict = AgentManager.verify(payload_dict)

    # 創建 ABM 帳號
    payload_dict = {
        'name':'admin',
        'password': 'admin'
    }
    ABMAccountManger.create(payload_dict)

    topic_name_str = "agents." + agent_uid_str
    payload_dict = {
        'topic_name':topic_name_str,
        'type': 'Central'
    }
    TopicSubscriber.subscribe(payload_dict)

    applications_metadata_list = metadatas_dict['applications']
    models_metadata_list = metadatas_dict['models']

    for application_metadata_dcit in applications_metadata_list:
        
        application_uid_str = application_metadata_dcit['uid']

        topic_name_str = "applications." + application_uid_str
        payload_dict = {
            'topic_name':topic_name_str,
            'type': 'Central'
        }
        TopicSubscriber.subscribe(payload_dict)

        payload_dict = application_metadata_dcit
        ApplicationMetadataWriter.create(payload_dict)

        for models_metadata_dict in models_metadata_list:
            f_application_uid_str = models_metadata_dict['f_application_uid']
            if application_uid_str == f_application_uid_str:
                payload_dict = models_metadata_dict
                print("great,", models_metadata_dict)
                ModelMetadataWriter.create(payload_dict)


    response_dict = {"detail":"Metadatas created successfully"}
    return JsonResponse(response_dict, status=200)

