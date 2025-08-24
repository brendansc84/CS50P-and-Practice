from twttr import shorten

def test_shorten():
    assert shorten("brendan") == "brndn"
    assert shorten("twitter") == "twttr"