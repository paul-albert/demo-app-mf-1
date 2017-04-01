import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    APP_HOST = '0.0.0.0'  # 0.0.0.0 - for external access, 127.0.0.1 - for internal only;
    APP_PORT = 5001
    SQLALCHEMY_DATABASE_URI = "postgresql://demo-app-mf-1:demo-app-mf-1@localhost/demo-app-mf-1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_PREFIX = '/api/'
    API_VERSION = 'v1.0'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
