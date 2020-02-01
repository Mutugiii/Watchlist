class Movie:
    '''
    Class for the movie to define movie objects
    '''
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        '''
        Initialize class variable objects
        '''
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
