"""
RESTful API URL Resources
"""
from flask import current_app as app
from flask_restplus import Resource
from werkzeug.utils import redirect
from app import base62
from . import api

@api.route('/<url>', methods=['GET', 'POST'])
class generateURL(Resource):
    @staticmethod

    @api.doc('generate-url', responses={200: 'url generated'})
    def post(self, url):
        """
        Generates new shortened URL 
        """

        # Generate new ID from database
        id = 321321321
        
        # Encode ID
        new_id = base62.toBase62(id)

        # Save id and url to database

        return {'url': 'http://localhost:8080' + new_id}
        # Save to database and return url to user


    @api.doc('retrieve-url', responses={200: 'url generated'})
    def get(self, url):
        """
        Retrieve and Redirect
        """

        # Retrieve original id from base62url
        id = base62.toBase10(url)


        # Get original url from database and redirect
        originalURL = "http://www.google.com"
        return redirect(originalURL, code = 302)
