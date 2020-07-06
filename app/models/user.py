""" 
EXAMPLE FILE
"""
from .db import *

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_int_seq'::regclass)"))
    discord_id = Column(BigInteger)
    token = Column(String(255))
