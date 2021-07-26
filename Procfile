release: python manage.py migrate --noinput
web: daphne WorldAtlas.asgi:application --port $PORT --bind 0.0.0.0
worker: REMAP_SIGTERM=SIGQUIT celery worker --app WorldAtlas.celery.app --loglevel info
