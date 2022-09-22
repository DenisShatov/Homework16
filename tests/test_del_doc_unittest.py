import unittest
from Task1 import del_doc
from parameterized import parameterized

fixture = [('11-2', True)]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(fixture)
    def test_people_name(self, ndoc, res):
        result = del_doc(ndoc)
        self.assertEqual(result, res)