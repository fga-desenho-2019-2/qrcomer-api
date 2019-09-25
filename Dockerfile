FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY requirements.txt requirements.txt

RUN apt-get update

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

ADD . .

EXPOSE 8000