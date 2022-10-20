import re

from sqlalchemy import create_engine
from pprint import pprint


# [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
connect_string = "mysql+mysqlconnector://root:root@127.0.0.1:3300/world"
engine = create_engine(connect_string)

pprint([attr for attr in dir(engine) if not re.match(r'__.*__', attr)])

select_all = """SELECT * FROM country"""
cursor = engine.execute(select_all)

print(f'\n{cursor}\n{type(cursor)}\n')
pprint([attr for attr in dir(cursor) if not re.match(r'__.*__', attr)])
print()

data = cursor.fetchall()
pprint(data)
print('\n'*2)



connect_string = "sqlite:///author_book_publisher.db"
engine = create_engine(connect_string)

select_all = """SELECT * FROM author"""
cursor = engine.execute(select_all)
data = cursor.fetchall()
print(*cursor.keys())
pprint(data)
