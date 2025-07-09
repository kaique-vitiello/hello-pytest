import pytest
from src.utils import clean_string

@pytest.fixture
def dirty_and_clean_strings():
    return [
        ("  Olá, mundo!  ", "olá, mundo!"),
        ("\tPython\n", "python"),
        ("  Teste   ", "teste"),
        ("", "")
    ]


def test_clean_string(dirty_and_clean_strings):
    for dirty, clean in dirty_and_clean_strings:
        assert clean_string(dirty) == clean


def test_clean_string_non_string():
    with pytest.raises(ValueError):
        clean_string(123)