# pull official base image
FROM python:3.6-slim

# set work directory
RUN mkdir -p /code/docker
WORKDIR /code

COPY . /code/
#install application
RUN apt-get update
RUN apk add-apt-repository ppa:ubuntugis/ppa &&  apt-get update
RUN apt-get install -y gdal-bin libgdal-dev
ARG CPLUS_INCLUDE_PATH=/usr/include/gdal
ARG C_INCLUDE_PATH=/usr/include/gdal
RUN pip install GDAL
# install dependencies

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN python3 -m pip install gunicorn --no-cache-dir
RUN python3 -m pip install -r requirements.txt --no-cache-dir

ENTRYPOINT /code/docker/docker-entrypoint.local.sh

# FROM python:3.6-alpine
#
# ENV PYTHONUNBUFFERED 1
# RUN mkdir -p /code/docker
# WORKDIR /code
#
# COPY . /code/
#
# RUN python3 -m pip install gunicorn --no-cache-dir
# RUN python3 -m pip install -r requirements.txt --no-cache-dir
#
# ENTRYPOINT /code/docker/docker-entrypoint.local.sh