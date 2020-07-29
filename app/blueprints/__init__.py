"""
Created by Epic at 7/8/20
"""
from . import punishments

from flask import Flask


def load(app: Flask):
    app.register_blueprint(punishments.blueprint)
