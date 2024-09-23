from kafka import KafkaConsumer
from main.utils.config import config
from main.apps.central_operation.services.abstract_metadata import ApplicationMetadataWriter
from main.apps.central_operation.services.file_metadata import ModelMetadataWriter
from main.apps.central_operation.services.central_operation import TopicSubscriber
import json

KAFKA_IP = config.KAFKA.HOST_IP
KAFKA_PORT1 = config.KAFKA.PORT1
KAFKA_PORT2 = config.KAFKA.PORT2
KAFKA_PORT3 = config.KAFKA.PORT3

KAFKA_BROKER1 = KAFKA_IP + ":" + KAFKA_PORT1
KAFKA_BROKER2 = KAFKA_IP + ":" + KAFKA_PORT2
KAFKA_BROKER3 = KAFKA_IP + ":" + KAFKA_PORT3

CENTRAL_KAFKA_SERVER = f"{KAFKA_BROKER1},{KAFKA_BROKER2},{KAFKA_BROKER3}"

def subscribe(topic_name_str):
    
    consumer = KafkaConsumer(
        bootstrap_servers=CENTRAL_KAFKA_SERVER
    )

    topic_list =  [topic_name_str]
    consumer.subscribe(topics=topic_list)

    for message in consumer:
        message_key = message.key.decode('utf-8')
        message_value_json = message.value.decode('utf-8')
        message_value_dict = json.loads(message_value_json)
        if message_key == "agent_delete":
            payload_dict = {}
            application_metadata_list = ApplicationMetadataWriter.filter_by_agent(payload_dict)

            for application_metadata_dict in application_metadata_list:
                application_uid_str = application_metadata_dict['uid']

                payload_dict = {'uid': application_uid_str}
                ApplicationMetadataWriter.delete(payload_dict)

        elif message_key == "application_add":
            application_metadata_dict = message_value_dict['application']
            model_metadata_list = message_value_dict['models']

            payload_dict = application_metadata_dict
            ApplicationMetadataWriter.create(payload_dict)
            payload_dict ={
                "topic_name":  "applications." + application_metadata_dict["uid"],
                "type":"Central"
            }  
            TopicSubscriber.subscribe(payload_dict)

            for model_metadata_dict in model_metadata_list:
                payload_dict = model_metadata_dict
                ModelMetadataWriter.create(payload_dict)

        elif message_key == "application_delete":
            application_uid_str = message_value_dict['application']

            payload_dict = {'uid': application_uid_str}
            ApplicationMetadataWriter.delete(payload_dict)

            payload_dict ={
                "topic_name":  "applications." + application_uid_str,
                "type":"Central"
            }  
            TopicSubscriber.unsubscribe(payload_dict)

        elif message_key == "application_update":
            application_metadata_dict = message_value_dict['application']

            payload_dict = application_metadata_dict
            ApplicationMetadataWriter.update(payload_dict)
        elif message_key == "model_add":
            model_metadata_dict = message_value_dict['model']

            payload_dict = model_metadata_dict
            ModelMetadataWriter.create(payload_dict)
        elif message_key == "model_update":
            model_metadata_dict = message_value_dict['model']

            payload_dict = model_metadata_dict
            ModelMetadataWriter.update(payload_dict)
        elif message_key == "model_delete":
            model_uid_str = message_value_dict['model']

            payload_dict = {'uid': model_uid_str}
            model_metadata_dict = ModelMetadataWriter.delete(payload_dict)

def unsubscribe():
    consumer = KafkaConsumer(
        bootstrap_servers=CENTRAL_KAFKA_SERVER
    )
    consumer.unsubscribe()
    