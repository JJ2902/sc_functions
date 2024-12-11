from lib.single_class_story import *
import pytest
# add_task method tests

# given an empty string 
# returns error message

def test_empty_string():
    task_tracker = Task_tracker()

    with pytest.raises(Exception) as e:
        task_tracker.add_task("")
    error = e.value
    assert str(error) == "Empty string given"
    

# given a non string
# returns an error message

def test_wrong_data_type():
    task_tracker = Task_tracker()

    with pytest.raises(TypeError) as e:
        task_tracker.add_task(4)
    error = e.value
    assert str(error) == "input must be a string"
    
# given a string 
# return append to todo_list and message "Task added"

def test_string_given_added_to_list():
    task_tracker = Task_tracker()
    result = task_tracker.add_task("Buy kimbap")
    assert result == "Buy kimbap added to todo list."

# see_todo_list Test

# Given an empty list
#returns error message

def test_empty_list():
    task_tracker = Task_tracker()

    with pytest.raises(Exception) as e:
        task_tracker.display_todo_list()
    error = e.value
    assert str(error) == "Todo list is empty."

# given list has more then 0 items
# returns formatted list

def test_display_todo_list():
    task_tracker = Task_tracker()

    task_tracker.add_task("Buy milk")
    
    result = task_tracker.display_todo_list()
    assert result == "Todo list:\nBuy milk"

# given list has more then 1 items
# returns formatted list

def test_display_todo_list_more_than_one():
    task_tracker = Task_tracker()

    task_tracker.add_task("Buy milk")
    task_tracker.add_task("Buy orange")
    
    result = task_tracker.display_todo_list()
    assert result == "Todo list:\nBuy milk\nBuy orange"

# mark_complete Test


# Given a string 
# returns if string in todo_list then append to complete List

def test_if_string_todo_list_append_complete_list():
    task_tracker = Task_tracker()

    task_tracker.add_task("Buy steak")
    
    # append to the complete list 

    # return "Task marked as complete!"
    result = task_tracker.mark_complete("Buy Steak")

    assert result == "Task marked as complete!"


# Given an empty list
#returns error message

def test_empty_list_completed():
    task_tracker = Task_tracker()

    with pytest.raises(Exception) as e:
        task_tracker.display_completed_list()
    error = e.value
    assert str(error) == "Completed list is empty."

# given list has more then 0 items
# returns formatted list

def test_display_completed_list():
    task_tracker = Task_tracker()

    task_tracker.add_task("Buy milk")
    task_tracker.mark_complete("Buy milk")
    result = task_tracker.display_completed_list()
    assert result == "Completed list:\nBuy milk"

# Given a string
# if string in the todo list then pop item
# return "Task has been deleted

def test_if_string_in_todo_list_pop_from_list():
    task_tracker = Task_tracker()

    task_tracker.add_task("Buy steak")
    
    # append to the complete list 

    # return "Task marked as complete!"
    result = task_tracker.delete_task_fr_todo_list("Buy steak")

    assert result == "Task deleted."
    # remove from todo list if match found
    # return "Task has been removed"

#Given task string not in list then return else statement

def test_else_statement_when_task_not_in_list():
    task_tracker = Task_tracker()

    task_tracker.add_task("Buy steak")

    result = task_tracker.delete_task_fr_todo_list("Buy fudge")

    assert result == "Task not found!"