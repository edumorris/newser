import os

class config:

    NEWS_BASE_URL = ''
    NEW_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig:
    pass

class DevConfig:
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}