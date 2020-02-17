FROM python:3.7-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
RUN python manage.py migrate
RUN python manage.py test polls
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin0', 'admin@example.com', 'adminadmin')" | python manage.py shell
