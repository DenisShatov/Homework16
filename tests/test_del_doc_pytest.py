from Task1 import del_doc
import pytest


@pytest.mark.parametrize('ndoc, result', [('11-2', True)])
def test_people_name(ndoc, result):
    res = del_doc(ndoc)
    assert res == result
