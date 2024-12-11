from lib.music_tracking import *
import pytest

#& add_track Method

#given a empty string
#returns exception handling error message

def test_empty_string_returns_error():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_track("")
    error = e.value
    assert str(error) == "Track name not given."

#given not string 
#returns another error message

def test_not_a_str():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_track(4)
    error = e.value
    assert str(error) == "Input string only."

def test_string_input_added_to_list():
    music_tracker = MusicTracker()

    result = music_tracker.add_track("Candle in the wind")

    assert result == "Candle in the wind added to recently played playlist."

# display_recently_played_playlist Method

#given empty RP playlist
#returns error message

def test_empty_list():
    music_tracker = MusicTracker()

    with pytest.raises(Exception) as e:
        music_tracker.display_recently_played_playlist()
    error = e.value
    assert str(error) == "Playlist is empty."

#given list has more then 0 tracks
#returns formatted list

def test_list_displays_when_not_empty():
    music_tracker = MusicTracker()

    music_tracker.add_track("Butterfly")
    music_tracker.add_track("Orange")

    result = music_tracker.display_recently_played_playlist()

    assert result == "Recently played tracks:\nButterfly\nOrange"