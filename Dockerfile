# syntax=docker/dockerfile:latest

FROM python:3.12.0-alpine3.18
WORKDIR /app
COPY ./ .
RUN <<EOF
pip install -r requirements.txt
apk add postgresql-client build-base postgresql-dev
EOF
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
