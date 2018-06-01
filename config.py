import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Parent config class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

class TestingConfig(Config):
    """Config for testing"""
    TESTING = True
    DEBUG = True

class DevelopmentConfig(Config):
    """Config for development"""
    DEBUG = True

app_config = {
    'testing':TestingConfig,
    'dvelopment':DevelopmentConfig,
}