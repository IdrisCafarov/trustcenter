#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket 127.0.0.1:3031 --chdir /home/app/app/ --wsgi-file app/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191