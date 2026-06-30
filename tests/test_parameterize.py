import pytest

def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize("input_value, expected", [
    (2, True),
    (4, True),
    (7, False),
    (11, False),
    (20, True)
])
def test_is_even(input_value, expected):
    assert is_even(input_value) == expected