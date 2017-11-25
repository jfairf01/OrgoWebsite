from flask import current_app
from flask_login import AnonymousUserMixin, UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(64), index=True)
    highScore = db.Column(db.Integer)

class HighScore(db.Model):
    __tablename__ = 'highScore'
    username = db.Column(db.String(64), index=True)
    highScore = db.Column()