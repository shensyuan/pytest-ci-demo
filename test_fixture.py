import pytest

@pytest.fixture
def sample_user():
    print("\n建立 user")

    return {
        "name": "Alice",
        "age": 20
    }


def test_name(sample_user):
    assert sample_user["name"] == "Alice"


def test_age(sample_user):
    assert sample_user["age"] == 20