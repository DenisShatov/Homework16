from Task2 import create_folder
import pytest


@pytest.mark.parametrize('folder, code', [('Netology1', 201),
                                           ('Netology2', 201),
                                           ('Netology3', 201)])
def test_create_folder(folder, code):
    result = create_folder(folder)
    assert code == result.status_code
