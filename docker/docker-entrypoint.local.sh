python3 -m pip install -r requirements.txt
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8019
