from lib.reading_time import *

#& 1. Describe the Problem
# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

#& 2. Design the Function Signature
# Include the name of the function, its parameters, return value, and side effects.
#def check_reading_time(text):
    #parameters:
    # text: a string containing words e.g "hello world"
    #? Return:
    #?  an estimate time as number based on the word count of the text in parameter
    #? E.g [60 minutes]
#    pass #Test-driving means no code here yet!

#& 3. Create Examples of Tests
#if we give an empty string
# it will give me a number

#!extract_number_minutes("")
# => 0

#if we give an string with more than or equal to 200 words
# it will give me a number of minutes based on wordcount
#!extract_number_minutes("A string with a lot of words")
# => number words

#if we give an string with less than 200 words
# it will give me a string to say less than a minute
# 
#extract_number_minutes("stringunder200words")
#  => "Less than a minute read!" 


#& 4. Implement the behaviour

#After each test you write. follow the test-driving process of red, green, refactor to omplent the behavoir


#if we give an empty string
# it will give me a number

#!extract_number_minutes("")
# => "No words to count"

def test_empty_string_given():
    result = check_reading_time("")
    assert result == "No words to count"


#if we give an string with more than or equal to 200 words
# it will give me a number words in text
#!extract_number_minutes("A string with a lot of words")
# => number words

# def test_string_with_200words_returns_number():
#     result = check_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a libero et dolor ullamcorper accumsan sit amet quis dolor. Donec non consectetur libero, nec pellentesque nibh. Pellentesque quis pellentesque lorem, a faucibus elit. Nunc sit amet quam a purus pretium semper a nec risus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse ut egestas nisl. Donec efficitur accumsan euismod. Maecenas elementum eget dolor ut sodales. In nec convallis massa. Nullam vehicula eget tortor vel ultricies. Donec sit amet nulla eget mi pulvinar elementum ac non ante. Aliquam erat volutpat. Curabitur a quam eu orci imperdiet imperdiet.Integer rutrum arcu at ante auctor, non interdum augue congue. Sed ut ipsum tortor. Integer nec pretium tellus. Morbi bibendum mauris leo, sit amet lobortis tellus fermentum et. Aenean tempor turpis et egestas pellentesque. Fusce consequat, lorem dictum hendrerit mattis, elit metus tempus dolor, vitae sollicitudin neque felis id augue. Mauris id diam vitae quam faucibus dictum. Praesent pretium lacus in nunc tincidunt convallis. Fusce vitae vulputate mi. Etiam a sapien sed magna molestie semper non a ante. Etiam rutrum mi urna, non feugiat neque finibus ac. Duis nec leo dui. Etiam consectetur pharetra odio et rhoncus. Mauris congue libero justo, eget rhoncus lacus.")
#     assert result == 204

#if we give an string with less than 200 words
# it will give me a string to say less than a minute
# 
#extract_number_minutes("stringunder200words")
#  => "Less than a minute read!" 

def test_word_count_less_than_200_words():
    result = check_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a libero et dolor ullamcorper accumsan sit amet quis dolor. Donec non consectetur libero, nec pellentesque nibh. Pellentesque quis pellentesque lorem, a faucibus elit. Nunc sit amet quam a purus pretium semper a nec risus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse ut egestas nisl. Donec efficitur accumsan euismod. Maecenas elementum eget dolor ut sodales. In nec convallis massa. Nullam vehicula eget tortor vel ultricies. Donec sit amet nulla eget mi pulvinar elementum ac non ante. Aliquam erat volutpat. Curabitur a quam eu orci imperdiet imperdiet.Integer rutrum arcu at ante auctor")
    assert result == "Less than a minute read!"

#if we give an string with more than or equal to 200 words
# it will give me a number of minutes based on wordcount
#!extract_number_minutes("A string with a lot of words")
# => number words

def test_string_with_200words_returns_number_in_minutes():
    result = check_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a libero et dolor ullamcorper accumsan sit amet quis dolor. Donec non consectetur libero, nec pellentesque nibh. Pellentesque quis pellentesque lorem, a faucibus elit. Nunc sit amet quam a purus pretium semper a nec risus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse ut egestas nisl. Donec efficitur accumsan euismod. Maecenas elementum eget dolor ut sodales. In nec convallis massa. Nullam vehicula eget tortor vel ultricies. Donec sit amet nulla eget mi pulvinar elementum ac non ante. Aliquam erat volutpat. Curabitur a quam eu orci imperdiet imperdiet.Integer rutrum arcu at ante auctor, non interdum augue congue. Sed ut ipsum tortor. Integer nec pretium tellus. Morbi bibendum mauris leo, sit amet lobortis tellus fermentum et. Aenean tempor turpis et egestas pellentesque. Fusce consequat, lorem dictum hendrerit mattis, elit metus tempus dolor, vitae sollicitudin neque felis id augue. Mauris id diam vitae quam faucibus dictum. Praesent pretium lacus in nunc tincidunt convallis. Fusce vitae vulputate mi. Etiam a sapien sed magna molestie semper non a ante. Etiam rutrum mi urna, non feugiat neque finibus ac. Duis nec leo dui. Etiam consectetur pharetra odio et rhoncus. Mauris congue libero justo, eget rhoncus lacus.")
    assert result == "1.02 minutes to read"