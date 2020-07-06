from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


Base = db.Model

Column = db.Column 
Interval = db.Interval
Integer = db.Integer
String = db.String
DateTime = db.DateTime
ForeignKey = db.ForeignKey
Boolean = db.Boolean
Date = db.Date
Text = db.Text
text = db.text
relationship = db.relationship
UniqueConstraint = db.UniqueConstraint
Float = db.Float
Table = db.Table
metadata = db.metadata
BigInteger = db.BigInteger
