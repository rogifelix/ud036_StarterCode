import webbrowser

# class Movie, object has attributes organized in order by: Title, Brief synopsis, Poster image, Youtube trailer
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # function to open the browser and show the respective trailer
    def show_trailer():
        webbrowser.open(trailer_youtube_url)
