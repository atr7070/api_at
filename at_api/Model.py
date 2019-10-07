from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class recommend_(db.Model):
    __tablename__="recommend_"

    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(100),nullable=False)
    interest = db.Column(db.String(50),nullable=False)

    def __init__(self, goal, interest):
        self.goal = goal
        self.interest = interest

class recommend_schema(ma.Schema):
    id = fields.Integer()
    goal = fields.String(required = True)
    interest = fields.String(required = True)
