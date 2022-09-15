# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/app

# Install dev requirements
COPY requirements-dev.txt .
RUN pip install --disable-pip-version-check -r requirements-dev.txt

# Install needed requirements
COPY requirements.txt .
RUN pip install --disable-pip-version-check -r requirements.txt

COPY . .

CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    # python manage.py createsuperuser --noinput || true && \
    python manage.py shell -i ipython && \
    python manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT}