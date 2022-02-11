#!/bin/bash

# celery -A app.celery worker --detach

gunicorn --worker-class=gevent --worker-connections=1000 --workers=9 -b 0.0.0.0:8000 "main:run_server(from_docker=True)"
# gunicorn --workers=9 --threads=4 -b 0.0.0.0:8000 "main:run_server(from_docker=True)"
