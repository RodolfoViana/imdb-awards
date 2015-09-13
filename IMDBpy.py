__author__ = 'Rodolfo Viana'

# Get the name of the movie.
import imdb
print 'movieId,movieTitle,movieDirector,movieRating,movieMetascore,listMovieCast'

ia = imdb.IMDb()
print 'a'
movie = ia.get_movie('0133093')
print movie[""]

