
from bank import value

def test_twenty_dollars():
    assert value("hey") == 20
    assert value("How are you doing?") == 20

def test_one_hundred_dollars():
    assert value("what's happening?") == 100
    assert value("shalom") == 100

def test_zero_dollars():
    assert value("hello") == 0
    assert value("hello, how are you?") == 0

