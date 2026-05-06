#!/bin/bash

cd url_shortner
pip install -r requirements.txt
python manage.py migrate
gunicorn url_shortner.wsgi:application --bind 0.0.0.0:$PORT
