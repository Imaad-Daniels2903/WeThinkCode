
from numb3rs import validate

def test_ip():
    assert validate("192.168.0.1") == True
    assert validate("1.1.1.1") == True
    assert validate("192.168.1") == False
    assert validate("192.168.256.21") == False
