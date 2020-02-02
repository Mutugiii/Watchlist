import os

class Config:
    '''
    General configuration parent class.
   '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration class

    Args:
        Config: The parent config with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class

    Args:
        Config: The parent conig with general configuration settings
    '''

    DEBUG = True

config_options = {
'development': DevConfig,
'production':ProdConfig
}
