#!/bin/bash

APP_PORT=${PORT:-8000}

cd /main/
/opt/venv/bin/gunicorn config.wsgi:application --bind "0.0.0.0:${APP_PORT}
"