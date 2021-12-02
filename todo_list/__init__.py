import os

import sqlalchemy
from flask import Flask, render_template, jsonify, request


def init_connect_engine():
    pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="postgresql+psycopg2",
                username=os.environ.get('POSTGRES_DB_USER'),
                password=os.environ.get('POSTGRES_DB_PSW'),
                database=os.environ.get('POSTGRES_DB_USER'),
                host=os.environ.get('SERVICE_POSTGRES_SERVICE_HOST')
            )
        )
    return pool


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    init_connect_engine()
    return app

    @app.route("/delete/<int:task_id>", methods=['POST'])
    def delete(task_id):
         try:
            # db_helper.remove_task_by_id(task_id)
            result = {'success': True, 'response': 'Removed task'}
         except:
            result = {'success': False, 'response': 'Something went wrong'}
         return jsonify(result)

    @app.route("/edit/<int:task_id>", methods=['POST'])
    def update(task_id):
        data = request.get_json()
        print(data)
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
        # db_helper.insert_new_task(data['description'])
        result = {'success': True, 'response': 'Done'}
        return jsonify(result)

    @app.route("/")
    def homepage():
        """ returns rendered homepage """
        from todo_list import database as db_helper
        items = db_helper.fetch_todo()
        return render_template("index.html", items=items)


app = create_app("/application/config.py")