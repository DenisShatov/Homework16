import unittest
from Task1 import move_doc
from parameterized import parameterized

fixture = [('11-2', '3', True)]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(fixture)
    def test_people_name(self, ndoc, ndir, res):
        result = move_doc(ndoc, ndir)
        self.assertEqual(result, res)
