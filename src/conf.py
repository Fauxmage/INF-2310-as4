import sqlite3 as sql


def reg_user(username, password):
    """ Inserts newly registered user into the database """
    
    conn = sql.connect("test.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO USERS (USERNAME,PASSWORD) VALUES (?,?)", (username,password))

    conn.commit()
    conn.close()


def return_user(username):
    """ Returns a user(pwd) to determine if passwords match """
    
    user_lookup = username

    conn = sql.connect("test.db")
    cur = conn.cursor()

    pwd_fetch = cur.execute("SELECT PASSWORD FROM USERS WHERE USERNAME=?", (user_lookup,))
    pwd = pwd_fetch.fetchone()

    if pwd:
        pwd_str = pwd[0].decode('utf-8')
        print("string:", pwd_str)
        pwd_byte = pwd_str.encode('utf-8')
        print("byte:", pwd_byte)
        return pwd_byte
    else:
        return False


    
