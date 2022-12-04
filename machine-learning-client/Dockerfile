# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

RUN pip install -U spacy
RUN pip install spacytextblob
RUN pip install pytest

RUN python -m textblob.download_corpora
RUN python -m spacy download en_core_web_sm

COPY . .

CMD [ "python3"]