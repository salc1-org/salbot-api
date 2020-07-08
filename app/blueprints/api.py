"""
Created by Epic at 7/8/20
"""
from flask import Blueprint

blueprint = Blueprint("test", __name__, url_prefix="/api")


@blueprint.route("/version")
def get_version():
    return {
        "version": 1
    }
