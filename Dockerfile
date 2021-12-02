

FROM python:3.8-slim as build
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT '/application'
RUN mkdir -p $APP_ROOT
WORKDIR $APP_ROOT

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-root -vvv
COPY todo_list todo_list
RUN poetry build


## Launch gunicorn
FROM python:3.8-slim as gunicorn
RUN pip install gunicorn
COPY config.py /application/config.py
COPY --from=build /application/dist/*.whl .

RUN pip install *.whl

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--log-level=debug", "todo_list:app"]
