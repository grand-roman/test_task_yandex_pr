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
        '5.0',
        '4.0',
        '2.0',
    ])
