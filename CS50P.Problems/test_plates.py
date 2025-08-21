from plates import is_valid

def test_is_valid():
    assert is_valid("HELLO") is True
    assert is_valid("HELLO, WORLD") is False
    assert is_valid("CS50P") is False
    assert is_valid("H") is False