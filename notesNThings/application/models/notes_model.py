from flask.ext.sqlalchemy import SQLAlchemy
from notesNThings.application.models.stub_database import stubNotes

import json

db = SQLAlchemy()

class Note (db.Model):
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'notes' 
    uid = db.Column(db.Integer, primary_key = True)
    stored_as = db.Column(db.String(64), unique=True)
    file_name = db.Column(db.String(32), unique=True)
    owner = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __init__(self, stored_as, file_name, owner, rating):
        self.stored_as = stored_as
        self.file_name = file_name
        self.owner = owner
        self.rating = rating

def getAllNotes():
    return json.dumps(stubNotes)