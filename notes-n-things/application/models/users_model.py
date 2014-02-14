#place proper imports here
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User (db.Model) 
	#define users table here for use by the model
	uid      = db.Column(db.Integer, primary_key = true)
	username = db.Column(db.String(32), unique=True)
    email    = db.Column(db.String(64), unique=True)
    password = db.Column(db.String())
    salt     = db.Column()
    admin    = db.Column(db.Boolean)

    def __init__(self, username, password, email):
        self.username = username
        self.pwdhash = generate_password_hash(password)
        self.email = email
        self.created = datetime.utcnow()
 
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)