from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, text
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pathlib import Path
from sys import path
from pprint import pprint

import re


# класс, от которого будут наследоваться модели
Base = declarative_base()


# модель таблицы связей таблиц author и publisher
author_publisher = Table(
    'author_publisher',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('author.author_id')),
    Column('publisher_id', Integer, ForeignKey('publisher.publisher_id'))
)
# модель таблицы связей таблиц book и publisher
book_publisher = Table(
    'book_publisher',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('book.book_id')),
    Column('publisher_id', Integer, ForeignKey('publisher.publisher_id'))
)


# модель класса для автора
class Author(Base):
    __tablename__ = 'author'
    id = Column('author_id', Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship('Book', backref=backref('book'))
    publishers = relationship('Publisher', secondary=author_publisher, back_populates='authors')

    def __repr__(self):
        return f"<name: '{self.first_name} {self.last_name}'>"


# модель класса для книги
class Book(Base):
    __tablename__ = 'book'
    id = Column('book_id', Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.author_id'))
    publishers = relationship('Publisher', secondary=book_publisher, back_populates='books')

    def __repr__(self):
        return f"<title: '{self.title}'>"


# модель класса для издательства
class Publisher(Base):
    __tablename__ = 'publisher'
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String)
    authors = relationship('Author', secondary=author_publisher, back_populates='publishers')
    books = relationship('Book', secondary=book_publisher, back_populates='publishers')


if __name__ == '__main__':
    db_path = Path(path[0]) / 'author_book_publisher.db'
    engine = create_engine(f"sqlite:///{db_path}")
    # engine.echo = True
    Session = sessionmaker(bind=engine)
    session = Session()

    # создаёт объект транзакции, формирует строку запроса
    result = session.query(Author)
    print(f'\n{result = }\n{type(result) = }\n')

    data = result.all()
    pprint(data)

    clancy = data[2]
    print(f'\n{clancy = }\n{type(clancy) = }\n')
    pprint([attr for attr in dir(clancy) if not re.match(r'__.*__', attr)])

    print(f'\n{clancy.books = }\n{type(clancy.books) = }\n')


    kings_books = (session.query(Book)
                          .join(Author)
                          .where(text('author.last_name = "King"'))
                          .all())
    pprint(kings_books)

    kings_books = (session.query(Author.last_name, Book.title)
                          .join(Book)
                          .where(text('author.last_name = "King"'))
                          .all())
    pprint(kings_books)
    print('\n'*2)

    publishers = session.query(Publisher).all()
    print(publishers, end='\n'*2)

    for each in publishers:
        print(each.name)
        print(each.authors)
        print(each.books, end='\n'*2)
