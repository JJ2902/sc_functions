# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

def check_reading_time(text):
    word_count = text.split()
    time_in_minutes = len(word_count)/200
    
    if len(word_count) > 200:
        return f"{time_in_minutes} minutes to read"
    elif len(word_count) == 0:
        return 'No words to count'
    else:
        return "Less than a minute read!"