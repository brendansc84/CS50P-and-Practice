import seasons

def test_seasons():
    assert seasons.numbers_to_words(0) == "zero"
    assert seasons.numbers_to_words(5) == "five"
    assert seasons.numbers_to_words(13) == "thirteen"
    assert seasons.numbers_to_words(85) == "eighty-five"
    assert seasons.numbers_to_words(523) == "five hundred twenty-three"
    assert seasons.numbers_to_words(1001) == "one thousand one"
    assert seasons.numbers_to_words(1234567) == "one million, two hundred thirty-four thousand, five hundred sixty-seven"
    assert seasons.numbers_to_words(-42) == "minus forty-two"
