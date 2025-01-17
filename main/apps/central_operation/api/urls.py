from django.urls import path
from main.apps.central_operation.actors import AgentLifeManager
from main.apps.central_operation.actors import ModelFileGeter
from main.apps.central_operation.actors import InferenceFileGeter
from main.apps.central_operation.actors import TopicSubscriber
from main.utils.config import config

CENTRAL_OPERATION_NAME=config.CENTRAL_OPERATION.NAME

urlpatterns = [
    path(
        f'{CENTRAL_OPERATION_NAME}/AgentLifeManager/init',
        AgentLifeManager.init
    ),
    path(
        f'{CENTRAL_OPERATION_NAME}/ModelFileGeter/download',
        ModelFileGeter.download
    ),
    path(
        f'{CENTRAL_OPERATION_NAME}/InferenceFileGeter/download',
        InferenceFileGeter.download
    ),
    path(
        f'{CENTRAL_OPERATION_NAME}/TopicSubscriber/subscribe',
        TopicSubscriber.subscribe
    ),
    path(
        f'{CENTRAL_OPERATION_NAME}/TopicSubscriber/unsubscribe',
        TopicSubscriber.unsubscribe
    ),
    path(
        f'{CENTRAL_OPERATION_NAME}/TopicSubscriber/resubscribe',
        TopicSubscriber.resubscribe
    )
]
