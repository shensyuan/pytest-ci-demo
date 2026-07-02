def test_name(sample_user):
    assert sample_user["name"] == "Alice"


def test_age(sample_user):
    assert sample_user["age"] == 20
