#!/bin/sh

FLASK_APP=blog.app python -m flask db upgrade \
    && python -m gunicorn -w 4 -b 0.0.0.0:8000 --access-logfile=- blog:app
