# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

ENV APP_ROOT '/application'
RUN mkdir -p $APP_ROOT

WORKDIR $APP_ROOT
COPY . $APP_ROOT

EXPOSE 5000

ENTRYPOINT gunicorn \
        --access-logfile="-"                   \
        --error-logfile="-"                    \
        --bind=0.0.0.0:5000                    \
        --worker-class=sync                    \
        --workers=1                            \
        --keep-alive=10                        \
        --graceful-timeout=10                  \
        todo_list:app