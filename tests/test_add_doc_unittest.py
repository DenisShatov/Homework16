import unittest
from Task1 import add_doc
from parameterized import parameterized

fixture = [('220', 'passport', 'Василий', '2', '2')]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(fixture)
    def test_people_name(self, ndoc, tdoc, nman, ndir, res):
        result = add_doc(ndoc, tdoc, nman, ndir)
        self.assertEqual(result, res)
