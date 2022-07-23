# Video controller: database connection


from db import get_db


def insert_video(name, duration, user_id, source, view, enabled):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO video(name, duration, user_id, source, view, enabled) VALUES(?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [name, duration, user_id, source, view, enabled])
    db.commit()
    return True


def update_video(id , name, duration, user_id, source, view, enabled):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE video SET name = ?, duration = ?, user_id = ?, source = ?, view = ?, enabled = ? WHERE id = ?"
    cursor.execute(statement, [name, duration, user_id, source, view, enabled, id])
    db.commit()
    return True


def delete_video(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM video WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, duration, user_id, source, view, enabled FROM video WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_videos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, duration, user_id, source, view, enabled FROM video"
    cursor.execute(query)
    return cursor.fetchall()