import hashlib
import os
import sqlite3


class Database:
    def __init__(self):
        self.PATH = "XploitHub_DB.db"


    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Exception as e:
            print(f"The error '{e}' occurred")
        return connection


    def create_users_table(self, connection):
        cur = connection.cursor()
        query = """CREATE TABLE users (
                email TEXT PRIMARY KEY,
                hashed_passw BLOB,
                salt BLOB,
                username TEXT
            
            )"""
        try:
            cur.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Exception as e:
            print(f"The error '{e}' occurred")


    def add_new_user(self, email, passw, username):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor

        # Hash the password and get the hashed password and salt
        hashed_password, salt = self.hash_password(passw)

        cur.execute("INSERT INTO users (email,hashed_passw,salt,username) VALUES (?,?,?,?)",
                    (email, hashed_password, salt, username))

        connection.commit()
        connection.close()


    def check_email_exists(self, email):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor
        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        result = cur.fetchone()

        return result is not None


    def check_sign_in(self, email, password):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor

        if self.check_email_exists(email):
            cur.execute("SELECT hashed_passw, salt FROM users WHERE email = ?", (email,))
            row = cur.fetchone()
            connection.close()

            if row:
                hashed_password, salt = row

                return self.verify_password(password, hashed_password, salt)

        connection.close()
        return False


    def get_username(self, email):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor

        cur.execute("SELECT username FROM users WHERE email = ?", (email,))
        username = cur.fetchone()[0]

        connection.close()
        return username


    def hash_password(self, password, salt_length=16, iterations=100000):
        # Generate a random salt
        salt = os.urandom(salt_length)

        # Hash the password using PBKDF2
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)

        # Return the hashed password and the salt
        return hashed_password, salt


    def verify_password(self, password, hashed_password, salt):
        # Hash the provided password with the same salt
        rehashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

        # Compare the hashed passwords
        return rehashed_password == hashed_password


    def create_history_table(self, connection):
        cur = connection.cursor()
        query = """CREATE TABLE history (
                email TEXT,
                scan_id TEXT,
                date TEXT,
                saved TEXT
    
            )"""
        try:
            cur.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Exception as e:
            print(f"The error '{e}' occurred")


    def add_new_scan_save(self, email, scan_id, date, save):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor

        cur.execute("INSERT INTO history (email,scan_id,date,saved) VALUES (?,?,?,?)",
                    (email, scan_id, date, save))

        connection.commit()
        connection.close()


    def get_history_save(self, email, date):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor

        cur.execute("SELECT saved FROM history WHERE email = ? AND date = ?", (email, date))
        saved_scan = cur.fetchone()[0]

        connection.close()
        return saved_scan


    def check_scan_id_exists(self, email, scan_id):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor

        cur.execute("SELECT * FROM history WHERE email = ? AND scan_id = ?", (email, scan_id))
        result = cur.fetchone()

        return result is not None


    def get_all_saved_dates(self, email):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor

        cur.execute("SELECT date FROM history WHERE email = ?", (email,))
        result = cur.fetchall()

        # Extract dates from tuples and convert them to date objects
        dates = [date[0] for date in result]

        return dates

    def print_all_database(self):
        connection = sqlite3.connect(self.PATH)  # Connect to Database
        cur = connection.cursor()  # Create a Cursor

        cur.execute("SELECT * FROM users")
        print(cur.fetchall())

        connection.close()


    def init_database(self):
        connection = self.create_connection(self.PATH)
        self.create_history_table(connection)
        self.create_users_table(connection)

        connection.close()


# db = Database()
#
# # Get the current date and time
# current_datetime = datetime.now()
# # Convert the datetime object to a string in a desired format
# curr_date = current_datetime.strftime("%Y-%m-%d %H:%M")
#
# all_dates = db.get_all_saved_dates("admin")
# print(all_dates)
#
# for one_date in all_dates:
#     print(db.get_history_save("admin", one_date[0]))
#
# print(db.check_scan_id_exists("admin", "17567563"))
#
# # db.add_new_scan_save("admin", "17567563", curr_date, "This really is the final save!")
