from mysql.connector import MySQLConnection, Error
from db_config import get_db_config
from sys import stderr
from typing import Optional
from pprint import pprint

import people


DEBUG = False

parameters = get_db_config()

Rows = Optional[list[tuple | dict]]
class DBHandler:
    def __init__(self):
        try:
            self.connection = MySQLConnection(**parameters)
            if DEBUG:
                if self.connection.is_connected():
                    print('Connection established')
        except Error as e:
            print(e, file=stderr)

    def select_query(self, query: str) -> list[tuple]:
        with self.connection.cursor() as cursor:
            if DEBUG:
                print(cursor)
            cursor.execute(query)
            return cursor.fetchall()

    def insert_query(self, query: str, arguments: Rows = None):
        with self.connection.cursor() as cursor:
            if DEBUG:
                print(cursor)
            if arguments is None:
                cursor.execute(query)
            else:
                cursor.executemany(query, arguments)
            self.connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


if __name__ == '__main__':
    select_query = "SELECT * FROM curators"

    insert_query = """
    INSERT curators 
        (Name, Surname) 
    VALUES
        (%s, %s)"""

    insert_named_query = """
    INSERT curators 
        (Name, Surname) 
    VALUES
        (%(name)s, %(surname)s)"""

    names = [
        ('Jim', 'Hopkins'),
        ('Serge', 'Benbow'),
        ('Bill', 'Flint'),
    ]

    with DBHandler() as dbh:
        pprint(dbh.insert_query(insert_named_query, people.data))
        pprint(dbh.select_query(select_query))

