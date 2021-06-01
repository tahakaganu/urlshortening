"""
URL Module
==========
"""
from flask_restplus import Namespace
api = Namespace('url', description='URL Shortening API')
from .resources import *
