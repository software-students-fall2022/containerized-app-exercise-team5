# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /machine-learning-client

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN python -m textblob.download_corpora
RUN python -m spacy download en_core_web_sm

COPY . .

CMD [ "python3"]