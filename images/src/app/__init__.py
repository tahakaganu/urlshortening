import os, socket
import validators
from flask import Flask, request, redirect
from flask_pymongo import PyMongo
from .base62 import toBase62, toBase10

App = Flask(__name__)

try:
    App.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE'] + '?authSource=admin' 
    mongo = PyMongo(App)
    db = mongo.db
    collection = db["urls"]
except Exception as e:
    print("There was an error trying to connect to the Mongo Database. Is it running?")
    print(e)
    exit(-1)

@App.route('/', methods=['POST'])
def encode():
    """
    Retrieve and Redirect
    """
    
    # Retrieve data
    data = request.get_json(force=True)
    url = data['url'].lower()

    if url[0:7] != "http://" and url[0:8] != "https://":
        url = "http://" + url

    if url == None or url == '':
        return {"message": "Invalid input format."}
    else:
        # Validate URL
        if validators.url(url):
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
        else:
            return {"message": "Invalid URL provided."}



@App.route('/<urlParam>', methods=['GET'])
def decode(urlParam):
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