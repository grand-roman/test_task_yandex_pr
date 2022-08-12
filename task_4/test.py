
import re


def test_name_func_make_divider_of(user_code):
    assert re.compile(
        r'def make_divider_of\(\w+\):'
    ).findall(
        user_code
    ), 'Проверьте, что вы создали функцию "make_divider_of"'


def test_name_func_div2(user_code):
    assert re.compile(
        r'div2 ='
    ).findall(
        user_code
    ), 'Проверьте, что вы создали функцию "div2"'


def test_name_func_div5(user_code):
    assert re.compile(
        r'div5 ='
    ).findall(
        user_code
    ), 'Проверьте, что вы создали функцию "div5"'


def test_name_func_division_operation(user_code):
    assert re.compile(
        r'def division_operation\(\w+\):'
    ).findall(
        user_code
    ), 'Проверьте, что вы создали вложенную функцию "division_operation"'


def test_return_func_division_operation(user_code):
    assert re.compile(
        r'return division_operation'
    ).findall(
        user_code
    ), 'Проверьте, что вы возвращаете вложенную функцию "division_operation"'


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
