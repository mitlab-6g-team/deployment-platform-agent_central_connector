import os
from dotenv import load_dotenv
from dataclasses import dataclass

# Initialization
load_dotenv(".env.common")
load_dotenv('.env', override=True)

@dataclass
class KafkaConfig:
    """
       Server config
    """
    HOST_IP: str
    PORT1: str
    PORT2: str
    PORT3: str

@dataclass
class ServerConfig:
    """
       Server config
    """
    HOST_IP: str
    PORT: str
    NAME: str
    VERSION: str


@dataclass
class Config:
    """
        Config sets
    """
    LOGS_FOLDER_PATH: str
    DJANGO_SETTINGS_MODULE: str
    DEBUG: str
    ALLOWED_HOSTS: str

    KAFKA: KafkaConfig
    AGENT_OPERATION:ServerConfig
    ABSTRACT_METADATA:ServerConfig
    FILE_METADATA:ServerConfig
    FILE_OPERATION:ServerConfig
    ENTRYPOINT:ServerConfig
    CENTRAL_OPERATION:ServerConfig


config = Config(
    #Default 
    LOGS_FOLDER_PATH=os.getenv("LOGS_FOLDER_PATH"),
    DJANGO_SETTINGS_MODULE=os.getenv("DJANGO_SETTINGS_MODULE"),
    DEBUG=os.getenv("DEBUG"),
    ALLOWED_HOSTS=os.getenv("ALLOWED_HOSTS"),
    # KAFKA
    KAFKA=KafkaConfig(
        HOST_IP=os.getenv("HTTP_KAFKA_HOST_IP"),
        PORT1=os.getenv("HTTP_KAFKA_PORT1"),
        PORT2=os.getenv("HTTP_KAFKA_PORT2"),
        PORT3=os.getenv("HTTP_KAFKA_PORT3"),
    ),
    # central-layer.agent_mgt.agent_connector.agent_operation
    AGENT_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_AGENT_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_AGENT_OPERATION_PORT"),
        NAME=os.getenv("HTTP_AGENT_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_AGENT_OPERATION_VERSION"),
    ),
    #agent-layer.agent_mgt.metadata_mgt.abstract_metadata
    ABSTRACT_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_ABSTRACT_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_ABSTRACT_METADATA_PORT"),
        NAME=os.getenv("HTTP_ABSTRACT_METADATA_NAME"),
        VERSION=os.getenv("HTTP_ABSTRACT_METADATA_VERSION"),
    ),
    #agent-layer.agent_mgt.metadata_mgt.file_metadata
    FILE_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_FILE_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_FILE_METADATA_PORT"),
        NAME=os.getenv("HTTP_FILE_METADATA_NAME"),
        VERSION=os.getenv("HTTP_FILE_METADATA_VERSION"),
    ),
    #agent-layer.agent_mgt.file_mgt.file_operation
    FILE_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_FILE_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_FILE_OPERATION_PORT"),
        NAME=os.getenv("HTTP_FILE_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_FILE_OPERATION_VERSION"),
    ),
    #agent-layer.agent_mgt.authenticate_middleware.entrypoint
    ENTRYPOINT=ServerConfig(
        HOST_IP=os.getenv("HTTP_ENTRYPOINT_HOST_IP"),
        PORT=os.getenv("HTTP_ENTRYPOINT_PORT"),
        NAME=os.getenv("HTTP_ENTRYPOINT_NAME"),
        VERSION=os.getenv("HTTP_ENTRYPOINT_VERSION"),
    ),
    #agent-layer.agent_mgt.central_connector.central_operation
    CENTRAL_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_CENTRAL_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_CENTRAL_OPERATION_PORT"),
        NAME=os.getenv("HTTP_CENTRAL_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_CENTRAL_OPERATION_VERSION"),
    )
)
