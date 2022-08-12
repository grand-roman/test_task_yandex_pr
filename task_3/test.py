import re


def test_cache_dict_exist(user_code):
    assert re.compile(
        r'\w+ = ({}|dict\(\))'
    ).findall(
        user_code
    ), 'Для кеширования хорошо подойдет словарь'


def test_cache_return(user_code):
    assert re.compile(
        r'return \w+\[\w+\]|return \w+\.get\(.+\)'
    ).findall(
        user_code
    ), 'Проверьте, возвращается ли кэш'


def test_precode_variables_exist(missing_variables):
    assert not missing_variables, (
        f'Пожалуйста, используйте переменные {", ".join(missing_variables)} '
        'из прекода.'
    )


def test_expected_imports_exist(missing_imports):
    assert not missing_imports, (
        f'Пожалуйста, импортируйте модуль {", ".join(missing_imports)}.'
    )


def test_stdout(author_output, student_output):
    if student_output:
        student_lines = student_output.strip().split('\n')
        author_lines = author_output.strip().split('\n')
        if len(author_lines) == len(student_lines):
            for line_num, (
                author_line, student_line
            ) in enumerate(
                zip(author_lines, student_lines),
                1
            ):
                assert author_line == student_line, (
                    'Результат не соответствует ожидаемому.\n'
                    f'Проверьте {line_num} строку результата '
                    'выполнения кода. Она должная выглядеть '
                    'следующим образом:\n'
                    f'{author_line}'
                )
    assert author_output == student_output, (
        'Результат не соответствует ожидаемому:\n'
        f'Ваш вывод:\n {student_output}\n'
        f'Ожидаемый вывод:\n {author_output}'
    )
