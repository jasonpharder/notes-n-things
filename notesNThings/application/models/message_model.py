from notesNThings.application.models import db
import json

class Message (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'messages'
    messageid = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String(455))
    posttime = db.Column(db.DateTime)
    courseid = db.Column(db.Integer, db.ForeignKey('courses.courseid'))
    userid = db.Column(db.Integer, db.ForeignKey('users.uid'))

    def __init__(self, message, posttime, courseid, userid):
        self.message = message
        self.posttime = posttime
        self.courseid = courseid
        self.userid = userid

    def course(self):
        return self.courseid

    def user(self):
        return self.userid