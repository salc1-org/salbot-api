from app.extensions import auth, ma
from app.models import User, db
from flask import request
import secrets
from flask_restful import Resource

class UserSchema(ma.Schema):                        # marshmallow schmea to easily jsonify
    class Meta:
        fields = ("id", "discord_id")               # exclude token
        

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserListResource(Resource):                   # resource for multiple users
    decorators = [auth.login_required]
    def get(self):                                  # gets all users, not paginatied, pagination would have to be custom added to using sqlalchemy paginate
        Users = User.query.all()
        return users_schema.dump(Users)

    def post(self):                                 # add new user, naive as it assumes correctly passed arguments
        new_user = User(
            discord_id=request.json['discord_id'],
            token=secrets.token_urlsafe(20)
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)

class UserResource(Resource):                       # resource for one user
    decorators = [auth.login_required]
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)
    
    def patch(self, user_id):                       # edit user
        user = User.query.get_or_404(user_id)

        if 'discord_id' in request.json:
            user.title = request.json['discord_id']

        db.session.commit()
        return user_schema.dump(user)

    def delete(self, user_id):                      # delete user
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204