from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(50) == "50%"