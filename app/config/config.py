import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    STEAM_API_KEY = '' # steam api key
    SECRET_KEY = '' # flask secret key
    SALT = '' # token salt


class ProductionConfig(Config):
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGOLAB_URI')
    }
    DEBUG = False
    REDIS_URL = os.environ.get('REDIS_URL')
    CELERY_BROKER_URL = os.environ.get('REDIS_URL')
    CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL')
    FRONTEND_URL = os.environ.get('FRONTEND_URL')


class StagingConfig(Config):
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGOLAB_URI')
    }
    DEVELOPMENT = True
    DEBUG = True
    REDIS_URL = os.environ.get('REDIS_URL')
    CELERY_BROKER_URL = os.environ.get('REDIS_URL')
    CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL')
    FRONTEND_URL = os.environ.get('FRONTEND_URL')


class DevelopmentConfig(Config):
    MONGODB_SETTINGS = {
        'host': "mongodb://localhost:27017/steamorganizerdb"
    }
    DEVELOPMENT = True
    DEBUG = True
    REDIS_URL = 'redis://localhost:6379'
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    FRONTEND_URL = 'http://localhost:9000/#/'
