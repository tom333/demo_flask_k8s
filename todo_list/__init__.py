import logging
import os

import sqlalchemy
from flask import Flask, render_template, jsonify, request
from flask.logging import default_handler

from todo_list import database as db_helper


def init_connect_engine():
    pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="postgresql+psycopg2",
                username=os.environ.get('POSTGRES_DB_USER'),
                password=os.environ.get('POSTGRES_DB_PSW'),
                database=os.environ.get('POSTGRES_DB_USER'),
                host=os.environ.get('SERVICE_POSTGRES_SERVICE_HOST'),
                port=os.environ.get('SERVICE_POSTGRES_SERVICE_PORT')
            )
        )
    with pool.connect() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS tasks ( \
    id SERIAL PRIMARY KEY, \
    task varchar(255) NOT NULL, \
    status varchar(30) );")
    return pool


app = Flask(__name__)
app.config.from_pyfile("/application/config.py")
app.db = init_connect_engine()
root = logging.getLogger()
root.setLevel(app.config["LOG_LEVEL"])
root.addHandler(default_handler)


@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
     try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
     except:
        result = {'success': False, 'response': 'Something went wrong'}
     return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    data = request.get_json()
    app.logger.debug(data)
    try:
        if "status" in data:
            # db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            # db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    app.logger.debug("index")
    items = db_helper.fetch_todo()
    app.logger.debug("test")
    return render_template("index.html", items=items)


app.logger.debug("Application démarée")
app.logger.info("Application démarée")
app.logger.error("Application démarée")