class MusicTracker:
    def __init__(self):
        self.recently_played = []

    def add_track(self,song):
        if song == "":
            raise Exception("Track name not given.")
        if type(song) != str:
            raise Exception("Input string only.")
        self.recently_played.append(song)
        return f"{song} added to recently played playlist."
    
    def display_recently_played_playlist(self):
        if len(self.recently_played) == 0:
            raise Exception("Playlist is empty.")
        
        recently_played_str = "Recently played tracks:"
        for track in self.recently_played:
            recently_played_str += f"\n{track}"
        return recently_played_str
        
music_tracker = MusicTracker()
music_tracker.add_track("Butterfly")

music_tracker.add_track("Orange")
print(music_tracker.recently_played)
print(music_tracker.display_recently_played_playlist())