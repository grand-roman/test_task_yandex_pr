import re

TEXT_TEMPLATE = [
    'Время выполнения функции: 1.0 с. 2', 
    'Время выполнения функции: 0.0 с. 2',
    'Время выполнения функции: 1.0 с. 4',
    'Время выполнения функции: 0.0 с. 4', 
    'Время выполнения функции: 0.0 с. 4'
]

def test_output(output):
    assert ' '.join(TEXT_TEMPLATE) in output, 'Проверьте правильность вывода функции "long_heavy". Возможно вы не использовали "wraps" в декорирующих ее функциях'

def test_cache_dict_exist(user_code):
    assert re.compile(r'\w+ = ({}|dict\(\))').findall(user_code), 'Для кеширования хорошо подойдет словарь'

def test_cache_return(user_code):
    assert re.compile(r'return \w+\[\w+\]|return \w+\.get\(.+\)').findall(user_code), 'Проверьте, возвращается ли кэш'

