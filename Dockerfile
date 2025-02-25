FROM python:3.12.0-alpine3.18
WORKDIR /everest_back
COPY ./ .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add postgresql-client build-base postgresql-dev curl
RUN python manage.py collectstatic