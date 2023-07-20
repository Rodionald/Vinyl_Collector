FROM python:3.11-slim

RUN mkdir -p /home/VinylCollector
ENV HOME=/home/VinylCollector
ENV APP_HOME=/home/VinylCollector/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .


