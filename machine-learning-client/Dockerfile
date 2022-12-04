# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /machine-learning-client

RUN python -m pip install --upgrade pip
RUN pip install pytest
RUN pip install spacy
RUN pip install spacytextblob
RUN python -m textblob.download_corpora
RUN python -m spacy download en_core_web_sm

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5001" ]
