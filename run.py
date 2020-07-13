import logging

from dotenv import load_dotenv

from app import config
from color_format import colorFormat

load_dotenv()
colorFormat(logging.getLogger())
from app import factory

factory.app.run("0.0.0.0", debug=config.DEBUG)
