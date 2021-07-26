release: python manage.py migrate --noinput
web: daphne WorldAtlas.asgi:application --port $PORT --bind 0.0.0.0
worker: python manage.py runworker channels --settings=WorldAtlas.settings -v2
