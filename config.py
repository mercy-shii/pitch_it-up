

class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mercy:shii@localhost/mercypitches'
     
    SECRET_KEY ='secret key'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development' :DevConfig,
    'production' :ProdConfig
}    