# Pull base image
FROM python:3.7 AS base

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y libproj-dev binutils curl git

# web app
RUN git clone https://github.com/yangnim21029/tfi101_medicalAssistant.git
RUN cd MedicalAssistant

# poetry套件相依與管理
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
RUN sudo apt-get install python3-distutils
ENV PATH "${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./

# download model
RUN apt-get update && apt-get install wget && wget https://storage.googleapis.com/tfi101linebot/main.tgz && \
    apt-get install tar && tar xvf main.tgz && \
    cd main

# Dev image
FROM base AS dev
RUN poetry install
COPY . /app/

# Prod image
FROM base AS prod
RUN poetry install --no-dev
COPY . /app/

#
VOLUME /app/MedicalAssistant
ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh""]
EXPOSE 3000
CMD python3 app.py
