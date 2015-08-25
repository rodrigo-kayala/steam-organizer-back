import os

from celery import Celery
from flask import Flask
from flask.ext.cors.extension import CORS
from flask.ext.mongoengine import MongoEngine
from flask.ext.openid import OpenID
import redis

app = Flask(__name__)
configenv = os.environ.get('APP_SETTINGS')
if not configenv:
    configenv = 'app.config.config.DevelopmentConfig'

app.config.from_object(configenv)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

cors = CORS(app)

db = MongoEngine(app)
oid = OpenID(app)
redis_conn = redis.from_url(app.config['REDIS_URL'])

from app.security.loginrest import loginrest
from app.collection.steamapprest import steamapprest

app.register_blueprint(loginrest, url_prefix='/rs')
app.register_blueprint(steamapprest, url_prefix='/rs')

if __name__ == '__main__':
    app.run()
