def make_snippit(string):
    if type(string) is not str:
        return "Not a string"
    #split the string
    word_list = string.split()
    if len(word_list) >= 5:
        return " ".join(word_list[:5]) + "..."
    else:
        return string
