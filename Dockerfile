FROM python:latest

# Config and Setup
WORKDIR /pac

# Dependencies
COPY requirements.txt dev-requirements.txt codecov.yml setup.py /pac/
COPY nlp/ /pac/nlp/

RUN pip install --no-cache-dir -r requirements.txt -r dev-requirements.txt
