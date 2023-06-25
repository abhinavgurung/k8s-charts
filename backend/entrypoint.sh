#!/bin/sh


gunicorn -b 0.0.0.0:5000 --workers 4 --threads 50 run:gunicorn_app
