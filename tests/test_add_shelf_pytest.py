from Task1 import add_shelf
import pytest


@pytest.mark.parametrize('ndir, result', [('4', True)])
def test_people_name(ndir, result):
    res = add_shelf(ndir)
    assert res == result
