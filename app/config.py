class Config:
    '''
    General configuration parent class.
    '''

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

