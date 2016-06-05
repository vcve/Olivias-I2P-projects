# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
# class instantiating section: {movie related information}

import fresh_tomatoes
# class instantiating section: {The movie website}

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Two imprisoned men bond over a number of years, finding solace and\
eventual redemption through acts of common decency.",
                                       "https://img1.doubanio.com/lpic/s27998208.jpg",  # noqa
                                       "https://www.youtube.com/watch?v=AAzVYa3L31M")  # noqa
leon = media.Movie("Leon",
                   "Mathilda, a 12-year-old girl, is reluctantly \
taken in by Léon, a professional assassin,after her family is \
murdered. Léon and Mathilda form an unusual relationship, as \
she becomes his protégée and learns the assassin's trade.",
                   "https://img3.doubanio.com/view/photo/photo/public/p2168338256.jpg",  # noqa
                   "https://www.youtube.com/watch?v=OFHoSvkfyRY")  # noqa


Ba_wang_bie_ji = media.Movie("Farewell My Concubine",
                             "The story of two men, who met as apprentices in the Peking Opera, and stayed\
friends for over 50 years.",
                             "https://upload.wikimedia.org/wikipedia/zh/0/0c/Bawangbieji.jpg",  # noqa
                             "https://www.youtube.com/watch?v=npNscbT5xwI")  # noqa


# appending movies into a list:
movies = [the_shawshank_redemption, leon, Ba_wang_bie_ji]

# calling the external rendering function:
fresh_tomatoes.open_movies_page(movies)
