from .models import User
import os
from flask_httpauth import HTTPTokenAuth
from flask_bootstrap import Bootstrap
from flask_restful import Api, Resource 
from flask_marshmallow import Marshmallow

ma = Marshmallow()

api = Api()

auth = HTTPTokenAuth(scheme='Bearer')
bootstrap = Bootstrap()

@auth.verify_token
def verify_token(token):
    user = User.query.filter_by(token=token).first()
    if user:
        return user.id
