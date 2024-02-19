FROM python:3-alpine

COPY /src /usr/src/app
WORKDIR /usr/src/app

RUN apk update && apk add \
        mariadb-client \
        mariadb-dev \
        mariadb-connector-c \
        gcc \
        gcompat \
        musl-dev

RUN pip install -r requirements.txt

ENTRYPOINT python __init__.py
