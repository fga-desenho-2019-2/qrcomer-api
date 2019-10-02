FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY requirements.txt requirements.txt

COPY ./compose/local/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

RUN apt-get update

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

ADD . .

EXPOSE 8000