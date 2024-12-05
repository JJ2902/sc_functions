from lib.snippit import *

# Given a string that is less than or equal to 5 words
#It returns string

def test_string_shorter_than_or_equal_5_words():
    result = make_snippit("This is a long sentence")
    assert result == "This is a long sentence..."


# Given a string that is more than 5 words
#It returns 5 words

def test_string_greater_than_5_words():
    result = make_snippit("This is a very long sentence")
    assert result == "This is a very long..."


# Given a 'string2' that is more than 5 words
#It returns 5 words

def test_another_string_greater_than_5_words():
    result = make_snippit("This is a second long string")
    assert result == "This is a second long..."

# Given a string that is more than 5 words
#It returns 5 words plus '...'

def test_string_greater_than_5_words_plus_three_dots():
    result = make_snippit("This is a second long string")
    assert result == "This is a second long..."

# Given a string that not a string
#It returns error message

def test_error_message_non_string():
    result = make_snippit(10)
    assert result == "Not a string"