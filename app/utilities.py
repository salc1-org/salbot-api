"""
Created by Epic at 7/14/20
"""
from functools import wraps

from flask import request, jsonify

from . import config


def require_authentication(func):
    @wraps(func)
    def inner_auth():
        if request.headers.get("Authorization", None) != config.API_TOKEN:
            return jsonify(success=False, message="Unauthorized"), 401
        return func()
    return inner_auth
