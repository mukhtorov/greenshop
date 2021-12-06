# syntax=docker/dockerfile:1
FROM python:3.9.6

WORKDIR /greenshop

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Europe/Moscow
ENV DEBIAN_FRONTEND="noninteractive"

COPY requirements.txt /greenshop/requirements.txt

# Set timezone
RUN ln -snf "/usr/share/zoneinfo/$TZ" /etc/localtime
RUN echo "$TZ" > /etc/timezone

# system deps
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev

RUN apt-get -y install tzdata
COPY Pipfile Pipfile.lock /greenshop/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile


COPY . /greenshop/