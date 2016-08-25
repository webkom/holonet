FROM python:3.5
MAINTAINER Abakus Webkom <webkom@abakus.no>

ENV PYTHONPATH /app/
ENV PYTHONUNBUFFERED 1
ENV ENV_CONFIG 1

RUN mkdir -p /app
COPY . /app/
WORKDIR /app

RUN set -e \
    && apt-get update \
    && apt-get autoremove -y \
    && apt-get clean \
    && pip install --no-cache -r requirements/prod.txt \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
