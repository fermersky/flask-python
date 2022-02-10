#!/usr/bin/env bash

docker rm -f flask

docker build -t flask-gunicorn .

docker run --name flask -p 8000:8000 -d flask-gunicorn

docker logs -f flask