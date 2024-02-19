FROM python:3-alpine

COPY /src /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
        libmariadb3 \
        libmariadb-dev \
        mariadb-client

RUN pip install -r requirements.txt

ENTRYPOINT python __init__.py
