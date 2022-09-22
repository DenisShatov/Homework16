import unittest
from Task1 import add_shelf
from parameterized import parameterized

fixture = [('4', True)]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(fixture)
    def test_people_name(self, ndir, res):
        result = add_shelf(ndir)
        self.assertEqual(result, res)
