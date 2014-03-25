from notesNThings.application.models import db
import json
from random import *

class Note (db.Model):
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'notes' 
    uid = db.Column(db.Integer, primary_key = True)
    stored_as = db.Column(db.String(64), unique=True)
    file_name = db.Column(db.String(32))
    owner = db.Column(db.Integer, db.ForeignKey('users.uid'))

    def __init__(self, stored_as, owner):
        self.stored_as = stored_as
        self.file_name = randint(10000000000000000000,100000000000000000000)
        self.owner = owner
