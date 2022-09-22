import unittest
from Task1 import people_name
from parameterized import parameterized

fixture = [('11-2', 'Геннадий Покемонов'),
           ('2207 876234', 'Василий Гупкин'),
           ('10006', 'Аристарх Павлов')]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(fixture)
    def test_people_name(self, number, res):
        result = people_name(number)
        self.assertEqual(result, res)
