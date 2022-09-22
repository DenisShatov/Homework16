from Task2 import create_folder
import unittest
from parameterized import parameterized


fixture = [('Netology1', 201),
           ('Netology2', 201),
           ('Netology3', 201)]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(fixture)
    def test_create_folder(self, folder, res):
        result = create_folder(folder)
        self.assertEqual(result, res)
