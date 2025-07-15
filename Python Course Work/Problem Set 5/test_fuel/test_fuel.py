
from pytest import raises
from fuel import convert, gauge

def test_convert():
    assert convert("50/100") == 50
    assert convert("1/10") == 10

def test_zero_division():
    with raises(ZeroDivisionError):
        convert("5/0")

def test_greater_numerator():
    with raises(ValueError):
        convert("5/4")


def test_negative_numbers():
    with raises(ValueError):
        convert("-11/10")
        convert("11/-10")
        convert("-6/-9")

def test_str_input():
    with raises(ValueError):
        convert("cat/dog")

def test_empty():
    assert gauge(1) == "E"

def test_full():
    assert gauge(99) == "F"

def test_gauge_output():
    assert gauge(50) == "50%"
    assert gauge(10) == "10%"
