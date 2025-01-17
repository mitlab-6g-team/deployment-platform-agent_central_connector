from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.utils.packet import unpacking
from django.http import JsonResponse
from main.apps.central_operation.services.abstract_metadata import TopicMetadataWriter
from main.apps.central_operation.services.central_operation import TopicSubscriber
from main.apps.central_operation.services.kafka import topic
from multiprocessing import Process
import os
import signal

@log_trigger("INFO")
@require_POST
def subscribe(request):
    data_dict = unpacking(request)

    topic_name_str = data_dict['topic_name']
    type_str = data_dict['type']

    process = Process(target=topic.subscribe, args=(topic_name_str,))
    process.start()
    print('process: ',process)
    consumer_process_pid_int = process.pid
    print(process)

    payload_dict = {
                    "consumer_process_pid": consumer_process_pid_int,
                    "name": topic_name_str,
                    "type":type_str
    }
    print('payload: ',payload_dict)
    TopicMetadataWriter.create(payload_dict)

    response_dict = {"detail":"Topic subscribed successfully"}
    return JsonResponse(response_dict, status=200)

@log_trigger("INFO")
@require_POST
def unsubscribe(request):
    data_dict = unpacking(request)

    topic.unsubscribe()

    topic_name_str = data_dict['topic_name']
    type_str = data_dict['type']
    payload_dict = {
        "name": topic_name_str,
        "type": type_str
    }
    metadata_dict = TopicMetadataWriter.retrieve(payload_dict)

    consumer_process_pid_int = metadata_dict['consumer_process_pid']
    print(consumer_process_pid_int)
    os.kill(consumer_process_pid_int, signal.SIGALRM)
    # payload_dict = {"consumer_process_pid": consumer_process_pid_int}
    TopicMetadataWriter.delete(payload_dict)

    payload_dict = {}
    topic_metadatas_list = TopicMetadataWriter.filter_by_agent(payload_dict)

    for topic_metadatas_dict in topic_metadatas_list:
        # consumer_process_pid_int = topic_metadatas_dict['consumer_process_pid']
        # payload_dict = {"consumer_process_pid": consumer_process_pid_int}
        topic_name_str = topic_metadatas_dict['name']
        type_str = topic_metadatas_dict['type']
        payload_dict = {
                        "name": topic_name_str,
                        "type":type_str
        }
        
        metadata_dict = TopicMetadataWriter.retrieve(payload_dict)

        consumer_process_pid_int = metadata_dict['consumer_process_pid']
        print(consumer_process_pid_int)
        os.kill(consumer_process_pid_int, signal.SIGALRM)

        TopicMetadataWriter.delete(payload_dict)
        


        topic_name_str = topic_metadatas_dict['name']
        type_str = topic_metadatas_dict['type']
        payload_dict = {
                        "topic_name": topic_name_str,
                        "type":type_str
        }
        TopicSubscriber.subscribe(payload_dict)

    response_dict = {"detail":"Topic unsubscribed successfully"}
    return JsonResponse(response_dict, status=200)


@log_trigger("INFO")
@require_POST
def resubscribe(request):

    print("aaa")
    topic.unsubscribe()
    print("bbb")
    payload_dict = {}
    topic_metadatas_list = TopicMetadataWriter.filter_by_agent(payload_dict)

    for topic_metadatas_dict in topic_metadatas_list:
        topic_name_str = topic_metadatas_dict['name']
        type_str = topic_metadatas_dict['type']
        payload_dict = {
                        "name": topic_name_str,
                        "type":type_str
        }

        TopicMetadataWriter.delete(payload_dict)
        
        payload_dict = {
                        "topic_name": topic_name_str,
                        "type":type_str
        }
        TopicSubscriber.subscribe(payload_dict)

    response_dict = {"detail":"Topic resubscribed successfully"}
    return JsonResponse(response_dict, status=200)