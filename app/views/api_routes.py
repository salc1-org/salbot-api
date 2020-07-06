from flask import Blueprint
from .api_routes import UserListResource, UserResource
from app.extensions import api
api_blueprint = Blueprint("api", __name__, url_prefix='/v1')


api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')

