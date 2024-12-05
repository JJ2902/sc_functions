from lib.count_words import *

# Given a string as an argument
#It returns string

# def test_string_returns_string():
#     result = count_words("string")
#     assert result == "string"

# Given a string that not a string
#It returns error message

def test_string_not_string():
    result = count_words(10)
    assert result == "Not a string"

# Given a string
#It returns num of words

def test_string_returns_word_count():
    result = count_words("This is long.")
    assert result == 3