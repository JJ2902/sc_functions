# 1.Describe the problem
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.


# 2. Design the function

def includes_todo(list):
    # Parameters:
    list of strings of to do items
    some items include the word '#TODO'

    #Returns
        boolean True or False

# 3. create example of test

#if we give an empty list
# it will give me a string catching error "nothing in list"

#if string has '#TODO'
return True

#if string does not have '#TODO'
return False

# Not a list error handling 
