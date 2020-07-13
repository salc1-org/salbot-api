"""
Created by Epic at 7/8/20
"""
import logging

from flask import Flask

import datadriver
from . import config
from .blueprints import load as load_blueprints

app = Flask(__name__)

app.logger = logging.getLogger(__name__)
app.db = datadriver.DatabaseClient(config.DATABASE_URI, False)

load_blueprints(app)
