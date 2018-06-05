# Movie Trailers
This is a simple trailer movie directory that lets you list movies and enable users view trailers of the movie. 

# How to run the code
To use this project you must have python installed on your computer. Once Python is installed follow the instructions below;

- Download the code or clone the repository 
- Open your terminal/command prompt and go the downloaded folder 
- Run the command -> `python entertainment_center.py`
- And Voila! the movie trailer website will open up in your default browser 
- Enjoy the trailers of my favourite movies :) . 

# How to add your own trailers
- Open the entertainment_center.py file and add your favourite trailers movies like so in this order ("movie title", "movie description", "movie Poster link", "movie trainer link from Youtube"); 
```
black_panther = media.Movie("Black Panther", 
					 "A 2018 American superhero film based on the Marvel Comics character", 
					 "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
					 "https://www.youtube.com/watch?v=xjDjIWPwcPU")
```


- Add the movie name in this case `black_panther` to the movies' list as show below
```
movies = [toy_story, avatar, titanic, coming_to_america, infinity_war, black_panther]
```
- Then go back to the terminal/command prompt and run the command `python entertaintment_center.py` again to see the updated website.


# License
The content of this repository is licensed under a [Creative Commons Attribution License](http://creativecommons.org/licenses/by/3.0/us/)