# pull official base image
FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV DEBUG 0

# set work directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

ENV PORT=8000
COPY . /app/
