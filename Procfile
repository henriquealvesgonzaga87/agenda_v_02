release: python manage.py migrate && python manage.py collectstatic
web: gunicorn agenda.wsgi --log-file -
