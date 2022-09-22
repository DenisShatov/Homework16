from Task1 import list_doc


def test_people_name():
    res = ['Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов']
    assert res == list_doc()