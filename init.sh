#!/bin/bash
set -e

cd src && FLASK_APP=server.py python -m flask db upgrade && newrelic-admin run-program gunicorn --worker-tmp-dir /dev/shm --workers=1 --threads=2 --graceful-timeout 20 --bind 0.0.0.0:3000 -k gevent wsgi:app
