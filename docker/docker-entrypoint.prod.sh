python manage.py collectstatic --no-input
python manage.py migrate --no-input
celery -A geoportal worker --concurrency=4 -l info &
gunicorn --bind 0.0.0.0:8019 geoportal.wsgi:application
