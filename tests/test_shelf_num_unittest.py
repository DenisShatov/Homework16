import unittest
from Task1 import shelf_num
from parameterized import parameterized

fixture = [('11-2', '1'),
           ('2207 876234', '1'),
           ('10006', '2')]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(fixture)
    def test_people_name(self, number, res):
        result = shelf_num(number)
        self.assertEqual(result, res)
