from lib.diary_entry import *
import math
import pytest

#& Given a empty title and content
#raises an error
def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    assert str(err.value) == "Diary entries must have a title or contents"

#& Given a title and content
#format returns a formatted entry, for example:
# "My Title: These are the contents"

def test_formats_title_and_content():
    myDiary = DiaryEntry("My Title", "contents")

    result = myDiary.format()
    assert result ==  "My Title: These are the contents"

#& Given a title and content
#count_words returns a int count of the number of words in the entry.
# title content returns int

def test_count_words_returns_word_count():
    myDiary = DiaryEntry("My Title", "food is food")
    
    result = myDiary.count_words()
    assert result == 5

#& Given a wpm
#reading_time returns a int count of the estimate reading time for the content at the given wpm
# wpm content returns int

def test_reading_time_returns_reading_time():
    myDiary = DiaryEntry("Entry One","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a libero et dolor ullamcorper accumsan sit amet quis dolor. Donec non consectetur libero, nec pellentesque nibh. Pellentesque quis pellentesque lorem, a faucibus elit. Nunc sit amet quam a purus pretium semper a nec risus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse ut egestas nisl. Donec efficitur accumsan euismod. Maecenas elementum eget dolor ut sodales. In nec convallis massa. Nullam vehicula eget tortor vel ultricies. Donec sit amet nulla eget mi pulvinar elementum ac non ante. Aliquam erat volutpat. Curabitur a quam eu orci imperdiet imperdiet.Integer rutrum arcu at ante auctor")

    myDiary.count_words()

    result = myDiary.reading_time(20)
    assert result ==  6

#? given a wpm of 0
#reading_time Raises error

def test_reading_time_wpm_of_zero():
    diary_entry = DiaryEntry("My Title", "one two three")
    with pytest.raises(Exception) as err_wpm:
        diary_entry.reading_time(0)
    assert str(err_wpm.value) == "Cannot calculate"

#& Given a content of six words
#And a wpm of 2
#And a minutes of 2
#reading_chunk returns the first four words

def test_reading_chunk_with_two_wpm_and_one_minute():
    diary_entry = DiaryEntry("My title", "one two four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"


#& Given a contents of six words
#And a wpm of 2 and 1 minute
#First time, #reading_chunk returns "one two"
#Next time, "three four"

def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2,2)
    assert result == "one two three four"


