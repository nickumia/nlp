FROM python:latest

# Config and Setup
WORKDIR /app

# Dependencies
COPY requirements.txt dev-requirements.txt codecov.yml setup.py /app/
COPY nlp/ /app/

RUN pip install -r requirements.txt -r dev-requirements.txt
