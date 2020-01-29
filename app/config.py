class Config:
    '''
    General configuration parent class.
   '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Production configuration class

    Args:
        Config: The parent config with General configuration settings
    '''

class DevConfig(Config):
    '''
    Development configuration class

    Args:
        Config: The parent conig with general configuration settings
    '''

    DEBUG = True

