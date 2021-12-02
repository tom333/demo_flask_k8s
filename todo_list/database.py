from flask import current_app


def fetch_todo() -> dict:
    conn = current_app.db.connect()
    current_app.logger.debug("connecte à la BDD")
    query_results = conn.execute("Select * from tasks;").fetchall()
    current_app.logger.debug("requete executée")
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)
    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    conn = current_app.db.connect()
    query = "Update tasks set task = '{}' where id = {};".format(text, task_id)
    conn.execute(query)
    conn.close()


def update_status_entry(task_id: int, text: str) -> None:
    conn = current_app.db.connect()
    query = "Update tasks set status = '{}' where id = {};".format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(text: str) -> int:
    conn = current_app.db.connect()
    query = "Insert Into tasks (task, status) VALUES ('{}', '{}') returning id;".format(
        text, "Todo")
    cur = conn.execute(query)
    task_id = cur.fetchone()[0]
    conn.close()

    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = current_app.db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close()