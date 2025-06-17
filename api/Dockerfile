FROM python:3.12-slim

WORKDIR /api

ADD requirements.txt .

ADD . api

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8011

CMD uvicorn api:app --port 8011

