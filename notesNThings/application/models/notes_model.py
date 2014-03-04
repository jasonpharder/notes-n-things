from flask.ext.sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class Notes (db.Model):
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
    notes = Notes.query.all()
    jsonTest = "{'test': { "
    print jsonTest
    for t in tests:
       jsonTest = jsonTest + json.dumps(t.file_name)
    return jsonTest