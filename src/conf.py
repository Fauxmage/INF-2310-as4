import sqlite3 as sql
#from db import create_db

def reg_user(username, password):
    """ Inserts newly registered user into the database """
    conn = sql.connect("test.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO USERS (USERNAME,PASSWORD) VALUES (?,?)", (username,password))

    conn.commit()
    conn.close()


def return_user(username):
    """ Returns a user(pwd) to determine if passwords match """
    pass
