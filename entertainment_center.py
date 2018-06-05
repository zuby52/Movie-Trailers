import media
import fresh_tomatoes

# Toy Story Movie: movie title, storyline, poster image and movie trailer
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar: movie title, storyline, poster image and movie trailer
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "http://www.youtube.com/watch?v=uZNHIU3uHT4")

# Titanic: movie title, storyline, poster image and movie trailer
titanic = media.Movie("Titanic",
                      "A fictionalized account of "
                      "the sinking of the RMS Titanic",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

# Coming To America: movie title, storyline, poster image and movie trailer
coming_to_america = media.Movie("Coming To America",
                                "A crown prince of Zamunda goes "
                                "to America to find his wife",
                                "https://upload.wikimedia.org/wikipedia/en/3/38/ComingtoAmerica1988MoviePoster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=fqfJqLFQSIk")

# Avengers -Infinity War: movie title, storyline, poster image
# and movie trailer
infinity_war = media.Movie("Avengers: Infinity War",
                           "In Avengers: Infinity War, the Avengers "
                           "and the Guardians of the Galaxy attempt"
                           "to stop Thanos from amassing the "
                           "all-powerful Infinity Stones",
                           "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# Black Panther: movie title, storyline, poster image and movie trailer
black_panther = media.Movie("Black Panther",
                            "A 2018 American superhero film based on "
                            "the Marvel Comics character",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

movies = [toy_story, avatar, titanic,
          coming_to_america, infinity_war, black_panther]

fresh_tomatoes.open_movies_page(movies)
