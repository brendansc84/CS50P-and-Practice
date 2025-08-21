from bank import value

def test_bank():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("sup") == 100