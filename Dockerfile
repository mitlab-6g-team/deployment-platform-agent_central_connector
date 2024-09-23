FROM python:3.8.10

WORKDIR /app/agent_central_connector

COPY . .

RUN apt-get update \
    && pip install -r /app/agent_central_connector/requirements/local.txt