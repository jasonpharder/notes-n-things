from notesNThings.application.models import db
from notesNThings.application.models.stub_database import stubUsers

import json

ROLE_USER = 0
ROLE_ADMIN = 1

class User (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique=True)
    email    = db.Column(db.String(64), unique=True)
    password = db.Column(db.String())
    admin    = db.Column(db.Boolean)

    def __init__(self, uid, username, password, email, admin):
        self.uid = uid
        self.username = username
        self.password = password
        self.email = email
        self.admin = admin

def getAllUsers():
    return json.dumps(stubUsers)