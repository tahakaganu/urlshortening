from flask import Flask, jsonify
from werkzeug.utils import redirect
from app.api.v1 import v1
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

App = Flask(__name__)

App.register_blueprint(v1)


@App.route('/')
def home():
    return redirect('v1/docs', code = 302)

@App.route('/v1')
def home():
    return redirect('v1/docs', code = 302)

if __name__ == '__main__':
    App.run()