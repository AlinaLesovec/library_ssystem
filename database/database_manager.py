import sqlite3

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect("database/library.db")
        self.cursor = self.connection.cursor()

        self.create_book_table()
        self.create_reader_table()
        self.create_loan_table()

    def create_book_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            isbn TEXT,
            year INTEGER,
            quantity INTEGER,
            available INTEGER
        )
        """)
        self.connection.commit()

    def create_reader_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS readers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            registration_date TEXT
        )
        """)
        self.connection.commit()

    def create_loan_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            reader_id INTEGER,
            loan_date TEXT,
            return_date TEXT,
            is_returned INTEGER
        )
        """)
        self.connection.commit()