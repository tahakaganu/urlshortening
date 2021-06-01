import os
from flask import Flask
from werkzeug.utils import redirect
from app.api.v1 import v1
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from flask_pymongo import PyMongo

App = Flask(__name__)

App.register_blueprint(v1)

App.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
mongo = PyMongo(App)
db = mongo.db

@App.route('/')
def home():
    return redirect('v1/docs', code = 302)

@App.route('/v1')
def home():
    return redirect('v1/docs', code = 302)

if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 8080)
    App.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)