FROM python:3.12.0-alpine3.18
WORKDIR /app
COPY ./ .
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt
RUN apk add postgresql-client build-base postgresql-dev
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
