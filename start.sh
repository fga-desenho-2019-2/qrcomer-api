#!/bin/bash

psql -U $PG_USER -d $PG_DB -h $PG_HOST -p $PG_PORT

while ! pg_isready -h $PG_HOST -p $PG_PORT -q -U $PG_USER -d $PG_DB
do
  >&2 echo "Postgres is unavailable - sleeping..."
  sleep 1
done

>&2 echo "Postgres is up - executing commands..."

python manage.py makemigrations
python manage.py migrate
python manage.py runserver