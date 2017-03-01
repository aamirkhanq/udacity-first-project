This is a simple site that displays a couple of movies and shows their trailer when you click on the posters. It makes use of class `Movie` in the `media.py` file.

### List of modules
- `media.py`: It contains the class `Movie`.
- `entertainment.py`: It creates instances of class `Movie` in the `media.py` module.
- `fresh_tomatoes.py`: It contains the function `open_movies_page()` that takes a list of movies as argument and renders an HTML.

### List of classes
There is just one class in the `media.py` module called `Movie`.
- `Movie`
  - **Instance variables**:
   1. `title`: Stores the title of movie represented by the object.
   2. `storyline`: Stores the storyline of the movie represented by the object.
   3. `poster_image_url`: Stores the URL of the poster of the movie represented by the object.
   4. `trailer_youtube_url`: Stores the YouTube URL of the trailer of the movie represented by the object.
  - **Instance Methods**:
   1. `show_trailer()`: Shows the trailer on YouTube when called. Takes no arguments. It is an object method.
