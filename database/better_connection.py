
from db_config import get_db_config
from mysql.connector import MySQLConnection, Error
from sys import stderr

DEBUG = True

parameters = get_db_config()

def db_connect():
    try:
        with MySQLConnection(**parameters) as connection:
            if DEBUG:
                if connection.is_connected():
                    print('Connection established')

    except Error as e:
        print(e, file=stderr)


if __name__ == '__main__':
    db_connect()