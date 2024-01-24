#!/usr/bin/env bash
# exit on error
set -o errexit
python3 -m pip install -r requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate

 echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('theadmin@example.com', 'password'); print(User.objects.all())" | python3 manage.py shell