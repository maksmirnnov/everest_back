# syntax=docker/dockerfile:latest

ARG EXPOSE_PORT=8000

FROM python:3.12.0-alpine3.18
WORKDIR /everest_back
COPY ./ .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add postgresql-client build-base postgresql-dev curl
RUN python manage.py collectstatic
EXPOSE ${EXPOSE_PORT}
