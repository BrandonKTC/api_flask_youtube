# User controller: database connection

from db import get_db


def insert_user(username, pseudo, email, password):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO user(username, pseudo, email, HASHBYTES(password)) VALUES(?, ?, ?, ?)"
    cursor.execute(statement, [username, pseudo, email, password])
    db.commit()
    return True


def update_user(id, username, pseudo, email):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE user SET username = ?, pseudo = ?, email = ? WHERE id = ?"
    cursor.execute(statement, [username, pseudo, email, id])
    db.commit()
    return True


def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM user WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, username, pseudo, email FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, username, pseudo, email FROM user"
    cursor.execute(query)
    return cursor.fetchall()
