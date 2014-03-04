from flask.ext.sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

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
    salt     = db.Column()
    admin    = db.Column(db.Boolean)

    def __init__(self, username, password, email, admin):
        self.username = username
        self.pwdhash = generate_password_hash(password)
        self.email = email
        self.created = datetime.utcnow()
        self.admin = admin
 
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

def getAllUsers():
    users = User.query.all()
    jsonTest = "{'test': { "
    print jsonTest
    for t in users:
       jsonTest = jsonTest + json.dumps(t.username)
    return jsonTest