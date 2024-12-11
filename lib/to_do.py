def includes_todo(my_list):
    if type(my_list) != list:
        raise Exception("Please enter valid data type")
    if len(my_list) != 0:
        if my_list:
            return any("#TODO" in item for item in my_list)
        else:
            return False
    else:   
        return "List is empty."
    
j_list = []
print(includes_todo(j_list))