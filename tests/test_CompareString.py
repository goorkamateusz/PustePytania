import pytest
from PustePytania.CompareString import CompareString as cs

example_pair = [
        ("abcdefghijk", "abcdefghijk", 0),
        ("Comare String 123", "Comare String 123", 0),
        ("abcdefghijk", "abcdefghij", 1),
        ("abcdefghijk", "00cdefghijk", 2),
        ("abcdefghijk", "cdefghi", 4),
        ("0123456789", "", 10),
        ("0123456789", "abcd", 10),
        ("0123456789", "23", 8),
    ]

@pytest.mark.parametrize("a,b,expected", example_pair)
def test_compare(a, b, expected):
    assert cs.compare( a, b ) == expected

@pytest.mark.parametrize("a,b,expected", example_pair)
def test_is_similar_for_zero_strickness(a, b, expected):
    expected = (expected == 0)
    assert cs.is_similar(a, b, 0) == expected

@pytest.mark.parametrize("a,b,expected", example_pair)
def test_is_similar_for_nozero_strickness(a, b, expected):
    strickness = 4
    expected = (expected <= strickness)
    assert cs.is_similar(a, b, strickness) == expected
