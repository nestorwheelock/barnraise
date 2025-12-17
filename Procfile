web: gunicorn barnraise.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate && python manage.py loaddata seed_data
