from lib.grammer_check import *

#& 1. User Story/ Describe the problem

# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

#& 2.Design the Function Signature

#def check_grammer(string):
    #parameters:
    # string: a string containing words e.g "hello world"
    #? Return:
    #?  a string stating if grammer rules were followed
    #? E.g Capital letter at the beginning
#    pass #Test-driving means no code here yet!

#& 3. Create Examples of Tests

#if we give an empty string
# it will give me a string catching error

#!extract_string_grammer("")
# => "Empty string"

#if we give an string with capital letter but no punctuation ending then
# it will return grammer alert.

#!extract_string_grammer("This is a sentence")
# => "Grammer Alert"

#if we give an string with no capital letter but a punctuation ending then
# it will return grammer alert.

#!extract_string_grammer("This is a sentence")
# => "Grammer Alert"

#if we give an string with capital letter but a punctuation ending then
# it will return grammer was followed.

#!extract_string_grammer("This is a sentence.")
# => "Grammer approved"

#& 4. Implement the behaviour i.e Test!

#if we give an empty string
# it will give me a string catching error

#!extract_string_grammer("")
# => "Empty string"

def test_empty_string():
    result = check_grammer("")
    assert result == "Empty string"

#if we give an string with capital letter but no punctuation ending then
# it will return grammer alert.

#!extract_string_grammer("This is a sentence")
# => "Grammer Alert"

def test_index_one_is_Capital():
    result = check_grammer("This is a sentence")
    assert result == "First letter is capital but does not end with a punctuation mark"

#if we give an string with capital letter but a punctuation ending then
# it will return grammer alert.

#!extract_string_grammer("This is a sentence")
# => "Grammer Alert"

def test_index_one_is_Capital_ends_in_puntuation():
    result = check_grammer("This is a sentence.")
    assert result == "First letter is capital and end with a punctuation mark"

#if we give an string with capital letter but a punctuation ending then
# it will return grammer alert.

#!extract_string_grammer("This is a sentence")
# => "Grammer Alert"

def test_index_one_is_not_Capital_but_ends_in_puntuation():
    result = check_grammer("this is a sentence.")
    assert result == "First letter is not capital and end with a punctuation mark"