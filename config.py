import os

class config:

    NEWS_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEW_API_KEY = os.environ.get('NEWS_API_KEY') #0ffd6c1788664312bcf394317d938e5e

class ProdConfig:
    pass

class DevConfig:
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}