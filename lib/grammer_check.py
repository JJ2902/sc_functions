def check_grammer(string):
    if not string:
        return "Empty string"
    
    first_char = string[0]
    last_char = string[-1]
    punc_char = '.!?'
    
    if first_char == first_char.upper():
        
        if last_char in punc_char:
            return "First letter is capital and end with a punctuation mark"
        else:
            return "First letter is capital but does not end with a punctuation mark"
    elif first_char != first_char.upper():
        if last_char in punc_char:
            return "First letter is not capital and end with a punctuation mark"
    else:
        return "First letter is not a capital"