# 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

noun: tasks
verb: add tasks, see list of tasks, mark task as complete, delete from list

# 2. Design the Class Interface

Class Task_Tracker():
    def __init__(self):
        self.todo_list = []
        self.completed = []

    def add_task():
        #parameter - a string
        #returns - append to todo_list

    def display_todo_list():
        #return - display the tasks in the todo list
        
    def mark_complete():
        #parameter - a task string
        #return - loop through the todo list and if match then append to completed list.

    def display_completed_task():
        #return - display the completed tasks in the complete list

    def delete_task_fr_todo_List():
        #parameter - a task string
        #return - loop through the todo list and if match then pop

3. Create Examples as Tests

# add_task method tests

# given an empty string 
# returns error message

def test_empty_string():
    returns "Empty string given"

# given a non string
# returns an error message

def test_wrong_data_type():
    returns "input must be a string"

# given a string 
# return append to todo_list and message "Task added"

def test_string_given_added_to_list():
    self.todo_list.append(string)
    returns "Task added"

# see_todo_list Test

# Given an empty list
#returns error message

def test_empty_list:
    return error message

# given list has more then 0 items
# returns formatted list

def test_display_todo_list():
    return list

# mark_complete Test


# Given a string 
# returns if string in todo_list then append to complete List

def test_if_string_todo_list_append_complete_list():
    append to the complete list 
    return "Task marked as complete!"


# Given a string
# if string in the todo list then pop item
# return "Task has been deleted

def test_if_string_in_todo_list_pop_from_list():
    remove from todo list if match found
    return "Task has been removed"

