import pytest
from PustePytania.ImageToText import *

@pytest.fixture
def test_text():
    return """
    o PRAWDA
    Odznacz mój wybór prawidłowy
    PRAWDA
    dadwasd FAŁSZ wynik
    O
    """

def test_clear_text_with_patterns(test_text):
    assert clear_text_with_patterns(test_text) == " prawidłowy wynik"
    