import unittest
from Task1 import list_doc


class TestFunctions(unittest.TestCase):
    def test_people_name(self):
        res = ['Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов']
        self.assertEqual(res, list_doc())
