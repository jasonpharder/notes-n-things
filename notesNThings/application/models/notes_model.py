from notesNThings.application.models import db
from notesNThings.application.models.stub_database import stubNotes

import json

class Note (db.Model):
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'notes' 
    uid = db.Column(db.Integer, primary_key = True)
    stored_as = db.Column(db.String(64), unique=True)
    file_name = db.Column(db.String(32), unique=True)
    owner = db.Column(db.Integer, db.ForeignKey('users.uid'))
    rating = db.Column(db.Integer)

    def __init__(self, uid, stored_as, file_name, owner, rating):
        self.uid = uid
        self.stored_as = stored_as
        self.file_name = file_name
        self.owner = owner
        self.rating = rating

def getAllNotes():
    return json.dumps(stubNotes)