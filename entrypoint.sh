#!/bin/sh

echo "Entrypoint started"

if [ "$DATABASE" = "postgres" ]; then
  echo "Waiting for postgres..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 1
  done

  echo "Postgres is ready"
fi

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"