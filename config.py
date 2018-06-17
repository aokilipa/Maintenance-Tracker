import os
from configparser import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))

filename = basedir+'/database.ini'
section = "postgresql"
#DATABASE_URL = "postgresql://antonio:pass.123@localhost/mtracker_db"
config_name = os.getenv('APP_SETTINGS')

class Config(object):
    """Parent config class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

class TestingConfig(Config):
    """Config for testing"""
    TESTING = True
    DEBUG = True
    section = "postgrestest"
    DATABASE_URL = "postgresql://antonio:pass.123@localhost/test_db"

class DevelopmentConfig(Config):
    """Config for development"""
    DEBUG = True
    DATABASE_URL = "postgresql://antonio:pass.123@localhost/mtracker_db"

class StagingConfig(Config):
    """Config for Staging"""
    DEBUG = True

class ProductionConfig(Config):
    """Config for production"""
    DEBUG = False
    TESTING = False

app_config = {
    'testing':TestingConfig,
    'development':DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}

def DATABASE_URL():
    if config_name == 'testing':
        return "postgresql://antonio:pass.123@/test_db"
    return "postgresql://antonio:pass.123@/mtracker_db"

def dbconfig(filename, section):
    #create a parser
    parser = ConfigParser()
    #read config file
    parser.read(filename)

    #get section, default to postgres
    db={}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('section {0} not found in the {1} file'.format(section,filename))
    return db