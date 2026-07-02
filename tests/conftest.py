import pytest
from src.user import create_user


@pytest.fixture
def sample_user():
    print("\nnew user")
    return create_user("Alice", 20)
