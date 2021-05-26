import os

class Config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'development key'
    PORT = os.getenv('port')



class LocalConfig(Config):
    DEBUG = True
    SECRET_KEY = 'development key'
    PORT = os.getenv('port') or 3001



class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'production key'
    PORT = os.getenv('port')


class TestingConfig(Config):

    DEBUG = False
    SECRET_KEY = 'testing key'
    PORT = os.getenv('port')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': LocalConfig,
    'testing':TestingConfig,
    }