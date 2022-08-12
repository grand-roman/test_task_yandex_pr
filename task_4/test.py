
import re

ANSWER_TEMPLATE = [
    '5.0',
    '4.0',
    '2.0',
]

def test_name_func_make_divider_of(user_code):
    assert re.compile(r'def make_divider_of\(\w+\):').findall(user_code), 'Проверьте, что вы создали функцию "make_divider_of"'

def test_name_func_div2(user_code):
    assert re.compile(r'div2 =').findall(user_code), 'Проверьте, что вы создали функцию "div2"'

def test_name_func_division_operation(user_code):
    assert re.compile(r'def division_operation\(\w+\):').findall(user_code), 'Проверьте, что вы создали вложенную функцию "division_operation"'

def test_return_func_division_operation(user_code):
    assert re.compile(r'return division_operation').findall(user_code), 'Проверьте, что вы возвращаете вложенную функцию "division_operation"'

def test_output(output):
    assert ' '.join(ANSWER_TEMPLATE) in output, 'Проверьте правильность вывода функций' 