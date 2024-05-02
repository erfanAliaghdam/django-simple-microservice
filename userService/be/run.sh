#!/bin/sh

set -e

if [ "$CONTAINER_ENV" = "local" ]; then
  echo "Running Commands For Local Environment ..."
  python manage.py wait_for_db
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver 0.0.0.0:8000
  echo "Running Commands For Local Environment Has Been Done."
elif [ "$CONTAINER_ENV" = "dev" ]; then
  echo "Running Commands For Development Environment ..."
  uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
  echo "Running Commands For Development Environment Has Been Done."
elif [ "$CONTAINER_ENV" = "release" ]; then
  echo "Running Commands For Release Environment ..."
  uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
  echo "Running Commands For Release Environment Has Been Done."
else
  echo "Running Commands For Production Environment ..."
  uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
  echo "Running Commands For Production Environment Has Been Done."
fi