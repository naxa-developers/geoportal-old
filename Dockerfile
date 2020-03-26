FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/docker
WORKDIR /code

COPY . /code/
RUN python3 -m pip install gunicorn --no-cache-dir
RUN python3 -m pip install -r requirements.txt --no-cache-dir

ENTRYPOINT /code/docker/docker-entrypoint.local.sh