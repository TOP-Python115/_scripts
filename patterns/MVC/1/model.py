"""Сущность Модель (MVC)."""

from dataclasses import dataclass
from pathlib import Path
from sys import path
from json import load as jload

script_dir = Path(path[0])
db_path = script_dir / 'people.json'


@dataclass
class Person:
    name: str
    age: int
    email: str = ''
    phone: str = ''
    country: str = ''
    langs: list[str] = None

    def __str__(self):
        return f'{self.name}'

    def does_speak(self, lang: str):
        return lang.upper() in self.langs

    @staticmethod
    def get_all() -> tuple['Person', ...]:
        with open(db_path, encoding='utf-8') as f_in:
            people = jload(f_in)
        result = ()
        for pers in people:
            pers['langs'] = pers['langs'].split()
            result += (Person(**pers), )
        return result
