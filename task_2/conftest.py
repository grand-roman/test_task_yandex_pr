from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent

@pytest.fixture(scope='module')
def user_code():
    with open(BASE_DIR / 'author.py', 'r') as f:
        return f.read()
    with open(BASE_DIR / 'precode.py', 'r') as f:
        return f.read()


@pytest.fixture(scope='module')
def output():
    return ' '.join([
        'Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891',
        'Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893'
    ])
