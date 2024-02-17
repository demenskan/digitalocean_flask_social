FROM python:3-alpine

COPY /src /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

ENTRYPOINT python __init__.py
