import pytest


@pytest.fixture
def sample_user():
    print("\nnew user")
    return {
        "name": "Alice",
        "age": 20,
    }
