import webbrowser


class Movie():
    """
    This class provides a way to store movies related information

    Attributes:
        VALID_RATINGS: a list store different movie ratings
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube_url):
        """
        This is the class constructor, it instantiates the class variables

        :param movie_title: string
        :param movie_storyline: string
        :param poster_image_url: string
        :param trailer_youtube_url: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Launches a webrowser and plays the movie trailer on Youtube"""
        webbrowser.open(self.trailer_youtube_url)
