import sqlite3
from sqlite3 import Error

def create_conection():
    try:
        conn = sqlite3.connect("licoreria.db")
        return conn
    except Error as e:
        print("Error 0: " + str(e))