import os, socket
from flask import Flask, request, jsonify
from werkzeug.utils import redirect
from flask_pymongo import PyMongo
from .base62 import toBase62, toBase10

App = Flask(__name__)

App.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE'] + '?authSource=admin' 
mongo = PyMongo(App)
db = mongo.db
collection = db["urls"]


@App.route('/', methods=['POST'])
def decode():
    """
    Retrieve and Redirect
    """
    
    # Retrieve data
    data = request.get_json(force=True)
    print(data)
    url = data['url']

    # Get max id from Database
    response = collection.find_one(sort=[("seq", -1)])

    # Generate new ID from database
    if response == None:
        id = 1
    else:
        id = int(response["seq"]) + 1

    # Generates new id
    urlCode = toBase62(id)

    # Saves to database
    collection.insert_one({"seq": id, "urlCode": urlCode, "url": url})

    return {"new_url": "http://" + socket.gethostname() + "/" + urlCode}
    # Get original url from database and redirect



@App.route('/<urlParam>', methods=['GET'])
def post(urlParam):
    """
    Decodes shortened URL and redirects
    """
  
    # Decode ID
    decoded_id = toBase10(urlParam)

    #Search database for correct url
    response = collection.find_one({"seq": decoded_id})


    # redirects user to correct url
    if response == None:
        return {"message": "URL does not exists."}
    else:
        return redirect(response["url"], 302)

    # return {'url': 'http://localhost:8080/' + new_id}
    # Save to database and return url to user




if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    App.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)