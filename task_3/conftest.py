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
        'Время выполнения функции: 1.0 с. 2', 
        'Время выполнения функции: 0.0 с. 2',
        'Время выполнения функции: 1.0 с. 4',
        'Время выполнения функции: 0.0 с. 4', 
        'Время выполнения функции: 0.0 с. 4'
    ])
