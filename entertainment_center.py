## Importing required modules
import media
import fresh_tomatoes

## Creating instances/objects of Movie class

swades = media.Movie("Swades",
                     "A NASA Scientist returns to India to work for his motherland",
                     "https://upload.wikimedia.org/wikipedia/en/5/5f/Swades_movie_poster.png",
                     "https://www.youtube.com/watch?v=NC7GuohSdWA")

raone = media.Movie("Ra.One",
                    "A villian and a hero from a video game escape outside to the real world",
                    "https://upload.wikimedia.org/wikipedia/en/5/58/Ra.Oneposter.jpg",
                    "https://www.youtube.com/watch?v=d9PlHc_qVKw")

mynameiskhan = media.Movie("My name is Khan",
                           "An autistic Muslim person goes on to meet the United States of America"
                           "to tell him that he is not a terrorist, after taking his wife's taunt too seriously",
                           "https://upload.wikimedia.org/wikipedia/en/5/5d/My_Name_Is_Khan_film_poster.jpg",
                           "https://www.youtube.com/watch?v=_uNDm6YfN2k")

raees = media.Movie("Raees",
                    "A person takes up the illegal business of alcohol in the Indian state of Gujarat",
                    "https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg",
                    "https://www.youtube.com/watch?v=8iv3ksZs0hk")

chakdeindia = media.Movie("Chak De India",
                          "A former Indian hockey team captain who was charged for deliberately"
                          "making India loose a match to Pakistan returns as the coach of the Indian women's hockey team"
                          "with a dream to make it win the World Cup",
                          "https://upload.wikimedia.org/wikipedia/en/0/0c/Chak_De%21_India.jpg",
                          "https://www.youtube.com/watch?v=6a0-dSMWm5g")

baazigar = media.Movie("Baazigar",
                       "When Vishwanath Sharma (Anant Mahadevan) loses his business to treacherous employee Madan Chopra (Dalip Tahil),"
                       "Sharma's son, Ajay (Shah Rukh Khan), vows to avenge him. While secretly dating Madan's daughter, Seema (Shilpa Shetty),"
                       "a disguised Ajay introduces himself to her father and her sister, Priya (Kajol), as businessman Vicky Malhotra, charming them both."
                       "After murdering Seema and making it look like a suicide, Ajay prepares to marry into Madan's family to complete his revenge.",
                       "https://upload.wikimedia.org/wikipedia/en/8/85/Baazigar_1993.jpg",
                       "https://www.youtube.com/watch?v=KzLdvd7ACv0")

## Creating a list of all the Movie objects/instances
movies = [swades, raone, mynameiskhan, raees, chakdeindia, baazigar]
fresh_tomatoes.open_movies_page(movies)
