"""
Created by Epic at 7/8/20
"""
from flask import Flask
import os
import logging
from .blueprints import load as load_blueprints

app = Flask(__name__)
logger = logging.getLogger("api.factory")

os.chdir("app")

load_blueprints(app)
