#!/bin/bash

set -o errexit
set -o nounset

>&2 echo "************ Starting server ************"

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000