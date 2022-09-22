from Task1 import add_doc
import pytest


@pytest.mark.parametrize('ndoc, tdoc, nman, ndir, result', [('112', 'invoice', 'Геннадий', '3', '3'),
                                                            ('220', 'passport', 'Василий', '2', '2'),
                                                            ('106', 'insurance', 'Аристарх', '3', '3')])
def test_people_name(ndoc, tdoc, nman, ndir, result):
    res = add_doc(ndoc, tdoc, nman, ndir)
    assert res == result

