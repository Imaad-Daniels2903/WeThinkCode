
from plates import is_valid

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("c") == False
    assert is_valid("csw1234") == False

def test_no_middle_numbers():
    assert is_valid("CA22YY") == False

def test_first_characters_not_aplhabetic():
    assert is_valid("22") == False
    assert is_valid("2A") == False
    assert is_valid("50CS") == False
    assert is_valid("5CS0") == False
    assert is_valid("C5S0") == False

def test_no_zero_as_firt_digit():
    assert is_valid("CS05") == False

def test_no_punctuation():
    assert is_valid("CS,50") == False
