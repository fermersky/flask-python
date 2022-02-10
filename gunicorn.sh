#!/bin/bash

gunicorn --worker-class=gevent --worker-connections=1000 --workers=9 -b 0.0.0.0:8000 "main:run_server(from_docker=True)"