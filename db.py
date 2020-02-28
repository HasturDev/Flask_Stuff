import sqlite3

class Database:
    connection = sqlite3.connect('schema.db')
    db_cursor = connection.cursor()