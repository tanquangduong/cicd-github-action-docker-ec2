from my_package.calculator import add, subtract


def test_add():
    assert add(1, 1) == 2
    assert add(1, -1) == 0
    assert add(1, 0) == 1
    assert add(0, 0) == 0
    assert add(0, 1) == 1
    assert add(0, -1) == -1
    assert add(-1, 0) == -1
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(1, 1) == 0
    assert subtract(1, -1) == 2
    assert subtract(1, 0) == 1
    assert subtract(0, 0) == 0
    assert subtract(0, 1) == -1
    assert subtract(0, -1) == 1
    assert subtract(-1, 0) == -1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
