import pytest
from src.even_utils import is_even


@pytest.mark.parametrize("input_value, expected", [
    (2, True),
    (4, True),
    (7, False),
    (11, False),
    (20, True),
])
def test_is_even(input_value, expected):
    assert is_even(input_value) == expected
