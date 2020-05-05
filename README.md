# Geoportal

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3-brightgreen.svg)](https://djangoproject.com)
[![CircleCI](https://circleci.com/gh/naxa-developers/geoportal/tree/master.svg?style=shield)](https://circleci.com/gh/naxa-developers/geoportal/tree/master)

GeoPortal facilitates searching and finding geospatial data and associated information services in Nepal and promotes geospatial data sharing in the country.

The Portal has been developed by Survey Department, Geographic Information Infrastructure Division (NGIID), Government of Nepal.

Setup Process

Simply copy local_settings_sample file to same directory of local_settings_sample naming local_settings.py.



#### Geoportal with Docker setup
```
For Development

cp local_settings_sample.py local_settings.py
docker build -t geoportal .
docker-compose up
Application will run on port 8019, you can change it from docker-compose.yaml file.

For Production 

cp local_settings_sample.py local_settings.py
docker build -t geoportal:0.1.0 -f prod.Dockerfile .
docker tag geoportal:0.1.0 geoportal/geoportal:0.1.0
docker-compose -f docker-compose-prod.yaml up -d
Application will run on port 8019

```
*Check logs ```docker-compose logs -f --tail 100```* <br>
*Django command shell ```docker exec -it geoportal_web python manage.py shell```* <br>
*Postgres command shell ```docker exec -it geoportal_postgres  psql -U postgres```* <br>


##### Alternatives Geoportal setup using virtualenvironment (If you are not familiar with docker)
```
Create virtual environment
Activate the environment
pip install -r requirements.txt
cp local_settings_sample.py local_settings.py
python manage.py runserver
```
