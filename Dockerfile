# syntax=docker/dockerfile:latest

FROM python:3.12.0-alpine3.18
WORKDIR /everest_back
COPY ./ .
RUN pip install -r requirements.txt
RUN apk add postgresql-client build-base postgresql-dev
EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
