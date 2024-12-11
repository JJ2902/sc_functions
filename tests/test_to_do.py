from lib.to_do import *
import pytest
#4 Implement the behaviours 

#if we give an empty list
# it will give me a string catching error "nothing in list"

# def test_if_empty_list():
#     result = includes_todo([])
#     assert result == "List is empty"

#if we give an list
# it will return list

def test_when_list_is_given_list_is_returned():
    result = includes_todo(["A","B", "C"])
    assert result == False

#if list of strings has '#TODO'
#return True

def test_if_item_in_list_has_certain_string():
    result = includes_todo(["A","B", "#TODOC"])
    assert result == True

# Not a list error handling 

def test_invalis_list():
    with pytest.raises(Exception) as err:
        includes_todo(4)
    error = err.value
    assert str(error) == "Please enter valid data type"
