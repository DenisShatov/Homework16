from Task1 import shelf_num
import pytest


@pytest.mark.parametrize('number, result', [('11-2', '1'),
                                    ('2207 876234', '1'),
                                    ('10006', '2')])
def test_people_name(number, result):
    assert shelf_num(number) == result
