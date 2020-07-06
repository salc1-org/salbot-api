import secrets
import os

from dotenv import load_dotenv
load_dotenv()


class ConfigClass(object):
    SECRET_KEY = secrets.token_hex(32)

    SQLALCHEMY_DATABASE_URI = os.environ["PG_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
