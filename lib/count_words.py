def count_words(string):
    if type(string) is not str:
        return "Not a string"
    word_list = string.split()
    return len(word_list)