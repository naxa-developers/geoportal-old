# pull official base image
FROM python:3.6-slim

LABEL Developer="Naxa pvt. ltd."
LABEL Address="Kathmandu, Nepal"
LABEL version="0.0.1"

# set work directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app/

#install application
RUN apt-get update && \
    apt-get install -y $(cat ./apt_req) && \
    apt-get clean

# install dependencies
RUN pip install --upgrade pip
RUN gdal-config --version
RUN pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`
RUN pip install -r requirements.txt && pip install gunicorn