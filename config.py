import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=c7e4aad3be1347a9aab0ecd2b4c850f5'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=c7e4aad3be1347a9aab0ecd2b4c850f5'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')




class ProdConfig(Config):
    
    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}