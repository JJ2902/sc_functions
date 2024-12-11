# 1.Describe the problem
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

noun: tracks
verb: add tracks, see the music track list

# 2. Design the Class

class MusicTracker:
    def __init__(self):
    self.recently_played = []

def add_track(song):
    # Parameters:
    Takes in a string of song name
    #Returns
    self.recently_played.append(song)
    return "track added to recently played"   

def display_recently_played_playlist(self):
   # return
    for loop over the items
    print("Recently played tracks:")
    for track in self.recently_play:
        print f"{track}"

# 3. create example of test

# add_track Method
#given a empty string
#returns exception handling error message

def test_empty_string_returns_error:
    pass

#given not string 
#returns another error message

def test_not_a_str:
    pass

#given a string as a song/track name
#returns "track added to recently played"

def test_string_input_added_to_list:
    pass

# display_recently_played_playlist Method

#given empty RP playlist
#returns error message

def test_empty_list:
    pass

#given list has more then 0 tracks
#returns formatted list

