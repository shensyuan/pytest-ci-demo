from calculator import add, sub

def test_add():
    assert add(3, 5) == 8

def test_sub():
    assert sub(10, 4) == 6