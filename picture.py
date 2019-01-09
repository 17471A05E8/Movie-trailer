import webbrowser

class cinema:
    def __init__(self,movie_names,movie_about_storyline,movie_clips_url,trailer_movie_youtube):
        self.title=movie_names
        self.storyline=movie_about_storyline
        self.poster_image_url=movie_clips_url
        self.trailer_youtube_url=trailer_movie_youtube
    def show_movie_trailers(self):
        webbrowser.open(self,youtubeurl)
    
                 
