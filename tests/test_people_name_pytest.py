from Task1 import people_name
import pytest


@pytest.mark.parametrize('number, result', [('11-2', 'Геннадий Покемонов'),
                                    ('2207 876234', 'Василий Гупкин'),
                                    ('10006', 'Аристарх Павлов')])
def test_people_name(number, result):
    assert people_name(number) == result
