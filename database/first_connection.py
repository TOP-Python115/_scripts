from mysql.connector import MySQLConnection, Error
from pprint import pprint

try:
    connection = MySQLConnection(
        user='root',
        password='root',
        host='127.0.0.1',
        port=3300,
        database='world'
    )
    print(connection)
    cursor = connection.cursor()
    cursor.execute('SELECT Code, Name FROM country LIMIT 10')
    results = cursor.fetchall()
    pprint(results)

except Error as e:
    print(e)
finally:
    cursor.close()
    print('cursor closed')
    connection.close()
    print('connection closed')
