import webbrowser


class Movie():
    """ This class stores the information about a movie."""

    def __init__(self,   
                 movie_title,
                 movie_storyline,
                 movie_poster,
                 movie_trailer):
        """Constructor to store the arguments to Class Variables. """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):  #A function which can be used to test youtube link 
        webbrowser.open(movie_trailer)
        
