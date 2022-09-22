from Task1 import move_doc
import pytest


@pytest.mark.parametrize('ndoc, ndir, result', [('11-2', '3', True)])
def test_people_name(ndoc, ndir, result):
    res = move_doc(ndoc, ndir)
    assert res == result
