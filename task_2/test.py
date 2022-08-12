import re

TESTS_FOR_CONTACT = [
    {
        'name': 'Михаил Булгаков',
        'address': 'Россия, Москва, Большая Пироговская, дом 35б, кв. 6',
        'phone': '2-03-27',
        'birthday': '15.05.1891'
    },
    {
        'name': 'Владимир Маяковский',
        'address': 'Россия, Москва, Лубянский проезд, д. 3, кв. 12',
        'phone': '73-88',
        'birthday': '19.07.1893'
    }
]

FORMAT_PARAMS = ["{self.name}", "адрес: {self.address}", "телефон: {self.phone}", "день рождения: {self.birthday}"]
FORMAT_TEMPLATE = "{name} — адрес: {address}, телефон: {phone}, день рождения: {birthday}"


def test_show_contact_output(output):
    for test_data in TESTS_FOR_CONTACT:

        assert FORMAT_TEMPLATE.format(
            name=test_data['name'], 
            phone=test_data['phone'], 
            birthday=test_data['birthday'], 
            address=test_data['address']
        ) in output, 'Проверьте, верно ли выведены контакты'


def test_name_func_show_contact(user_code):
    assert re.compile(r'def show_contact\(self\):').findall(user_code), 'Проверьте, что вы создали для класса Contact новый метод "show_contact"'


def test_body_show_contact_output(user_code):
    for format_param in FORMAT_PARAMS:
        assert re.compile(format_param).findall(user_code), f"Нет вывода параметра {format_param.split('{')[-1].split('}')[0]}"


def test_body_show_contact_foramt(user_code):
    temp = f"{FORMAT_PARAMS[0]} — {', '.join(FORMAT_PARAMS[1:])}"
    assert re.compile(rf'print\(f\"{temp}\"\)').findall(user_code), 'Нерпавильный формат для "show_contact"'
    

def test_print_contact_not_exist(user_code):
    assert re.compile(r'def print_contact\(\):\n').findall(user_code) == [], 'Проверьте, что удалили функцию "print_contact()" из кода'
    assert re.compile(
        r'print\(f\"{(mike|vlad).name} — адрес: {(mike|vlad).address}, телефон: {(mike|vlad).phone}, день рождения: {(mike|vlad).birthday}\"\)'
    ).findall(user_code) == [], 'Проверьте, что удалили функцию "print_contact()" из кода'

def test_call_method(user_code):
    assert re.compile(r'vlad.show_contact\(\)').findall(user_code), 'Проверьте, что обратились к методу "show_contact" объекта "vlad"'
    assert re.compile(r'mike.show_contact\(\)').findall(user_code), 'Проверьте, что обратились к методу "show_contact" объекта "mike"'
