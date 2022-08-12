import inspect
import sys
from collections import namedtuple
from io import StringIO
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent


@pytest.fixture(scope='module')
def user_code():
    with open(BASE_DIR / 'author.py', 'r') as f:
        return f.read()
    with open(BASE_DIR / 'precode.py', 'r') as f:
        return f.read()


@pytest.fixture(scope='session')
def get_precode_stdout():
    _stdout = sys.stdout
    sys.stdout = _stringio = StringIO()
    import precode
    output = _stringio.getvalue()
    sys.stdout = _stdout
    return (precode, output)


@pytest.fixture
def precode(get_precode_stdout):
    return get_precode_stdout[0]


@pytest.fixture
def student_output(get_precode_stdout):
    return get_precode_stdout[1]


@pytest.fixture
def author_output(output_param):
    import author
    return output_param.readouterr().out


def _get_divider(div_name, precode):
    try:
        divider = (
            inspect.getclosurevars(
                precode.__dict__[div_name]
            )
            .nonlocals['divider']
        )
    except KeyError:
        divider = None
    return divider


def _get_namedtuple():
    return namedtuple('Div', ('name', 'expected_arg', 'divider'))


@pytest.fixture
def divs(precode):
    d_iv = _get_namedtuple()
    return (
        d_iv('div2', 2, _get_divider('div2', precode)),
        d_iv('div5', 5, _get_divider('div5', precode))
    )
