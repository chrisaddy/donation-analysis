FROM ubuntu:16.04
FROM python:3.7.0

WORKDIR /app
ADD . /app

RUN pip install requirements.txt

CMD ['app.py']
