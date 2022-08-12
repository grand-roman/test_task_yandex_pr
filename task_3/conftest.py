import sys
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


@pytest.fixture
def missing_variables(precode):
    expected_variables = ('time_check', 'cache_args')
    missing_variables = []
    for var in expected_variables:
        if var not in precode.__dict__:
            missing_variables.append(var)
    return missing_variables


@pytest.fixture
def missing_imports(precode):
    expected_imports = ('time',)
    missing_imp = []
    for module_name in expected_imports:
        if module_name not in precode.__dict__:
            missing_imp.append(module_name)
    return missing_imp
