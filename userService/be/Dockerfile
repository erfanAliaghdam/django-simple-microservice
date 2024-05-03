FROM python:3.10

LABEL maintainer="aliaghdam.erfan@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

COPY ./requirements.dev.txt /tmp/requirements.dev.txt

COPY ./run.sh /scripts/run.sh

EXPOSE 8000

RUN python -m venv /py

RUN /py/bin/pip install --upgrade pip

RUN apt-get update -y

RUN /py/bin/pip install -r /tmp/requirements.txt --use-pep517

RUN if [ $DEV = "true" ]; \
      then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi

RUN adduser --disabled-password --no-create-home dj-microservice-user

RUN rm -rf /tmp

COPY . .

RUN chmod -R +x /scripts

RUN chown -R dj-microservice-user:dj-microservice-user /scripts

RUN chown -R dj-microservice-user:dj-microservice-user .

ENV PATH="/scripts:/py/bin:$PATH"

USER dj-microservice-user
