# pull official base image
FROM python:3

# set work directory
WORKDIR /opt/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
COPY Accion-Labs .
# install dependencies
COPY requirements.txt /opt/app

RUN pip3 install -r /opt/app/requirements.txt

ENV PORT=8000
