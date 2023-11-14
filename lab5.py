from flask import Blueprint, render_template, request, redirect, url_for
import psycopg2


lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "knowledge_base",
        user = "karina_makhmad_knowledge_base",
        password = "123")
    
    return conn;

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5')
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return "go to console"

