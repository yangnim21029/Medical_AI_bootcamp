# Pull base image
FROM python:3.7 AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

RUN apt-get update
RUN apt-get install -y libproj-dev binutils curl

# poetry套件相依與管理
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH "${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./

# Dev image
FROM base AS dev
RUN poetry install
COPY . /app/

# Prod image
# FROM base AS prod
# RUN poetry install --no-dev
# COPY . /app/
