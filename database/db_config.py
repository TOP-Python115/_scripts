from configparser import ConfigParser
from pathlib import Path
from sys import path

DEBUG = False

SCRIPT_DIR = Path(path[0])
ini_path = SCRIPT_DIR / 'db_config.ini'

database = 'mysql'

def get_db_config() -> dict:
    config = ConfigParser()
    config.read(ini_path, encoding='utf-8')
    if DEBUG:
        print(config.sections())
    if database in config:
        if DEBUG:
            print(dict(config[database]))
        result = dict(config[database])
        if 'port' in result:
            result['port'] = config.getint(database, 'port')
        return result
    else:
        raise ValueError(f'{database} is not found in {ini_path.name}')


if __name__ == '__main__':
    print(get_db_config())
