from flask import Blueprint
from flask_restplus import Api

from .url import api as url

v1 = Blueprint('api_v1', import_name=__name__, url_prefix='/v1')
api = Api(v1, title='Url Shorting API', version='v1', docs='/docs')

api.add_namespace(url, path='/url')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occured.'
    return {'message': message}, 500