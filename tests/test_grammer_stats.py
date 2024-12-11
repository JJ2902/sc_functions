from lib.grammerStats import *
import pytest

#& Given a empty text
#raises an error

def test_empty_text_error():
    grammerStat = GrammarStats()

    with pytest.raises(Exception) as e:
        grammerStat.check("")
    error = e.value    
    assert str(error) == "No text"

#& Given a string
#check returns true if first letter is upper and ends with punctuation mark

def test_string_returns_boolean_if_first_letter_cap_ends_in_punctuation_mark():
    grammerStat = GrammarStats()

    result = grammerStat.check("The whale.")
    assert result == True

def test_string_returns_False_if_first_letter_cap_ends_not_in_punctuation_mark():
    grammerStat = GrammarStats()

    result = grammerStat.check("The whale")
    assert result == False

def test_string_returns_False_if_first_letter_not_cap_ends_in_punctuation_mark():
    grammerStat = GrammarStats()

    result = grammerStat.check("the whale.")
    assert result == False

    #& Given a string
#check returns int which represents a percentage.

# def test_percentage_read_of_text():
#     grammerStat = GrammarStats()
#     sentences = ["The whale is swimming. the sea is blue. The sky is also blue."]

#     for sentence in sentences:
#         grammerStat.check("The whale is swimming. the sea is blue. The sky is also blue.")

#     result = grammerStat.percentage_good([sentence])
#     assert result == "2%"

def test_percentage_read_of_text():
    grammerStat = GrammarStats()
    sentences = [
        "The Whale is swimming. the sea is blue. The sky is also blue.",
        "hello world",
        "Python is awesome!"
]

    for sentence in sentences:
        grammerStat.check(sentence)

    result = grammerStat.percentage_good([sentence])
    assert result == "75%"
