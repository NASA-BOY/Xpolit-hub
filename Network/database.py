import sqlite3

PATH = "XploitHub_DB.db"


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")
    return connection


def create_users_table(connection):
    cur = connection.cursor()
    query = """CREATE TABLE users (
            email TEXT,
            passw TEXT,
            username TEXT
        
        )"""
    try:
        cur.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")


def add_new_user(email, passw, username):
    connection = sqlite3.connect(PATH)  # Connect to Database
    cur = connection.cursor()  # Create a Cursor

    cur.execute("INSERT INTO users (email,passw,username) VALUES (?,?,?)",
                (email, passw, username))

    connection.commit()
    connection.close()


def check_email_exists(email):
    connection = sqlite3.connect(PATH)  # Connect to Database
    cur = connection.cursor()  # Create a Cursor
    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cur.fetchone()

    return result is not None

def check_sign_in(email, passw):
    connection = sqlite3.connect(PATH)  # Connect to Database
    cur = connection.cursor()  # Create a Cursor

    if check_email_exists(email):
        cur.execute("SELECT passw FROM users WHERE email = ?", (email,))
        result = cur.fetchone()[0]

        connection.close()
        return passw == result

    connection.close()
    return False

def print_all_database():
    connection = sqlite3.connect(PATH)  # Connect to Database
    cur = connection.cursor()  # Create a Cursor
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())

    connection.close()


def init_database():
    connection = create_connection(PATH)
    create_users_table(connection)

    connection.close()


print(check_sign_in("barry@allen.com", "1234"))
