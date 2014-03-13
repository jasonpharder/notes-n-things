from notesNThings.application.models import db
from notesNThings.application.models.stub_database import stubCourses

import json

class Course (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'courses'
    courseid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(9))
    alt_name = db.Column(db.String(255))
    professor = db.Column(db.Integer)

    def __init__(self, name, alt_name, professor):
        self.name = name
        self.alt_name = alt_name
        self.professor = professor

def getAllCourses():
    return json.dumps(stubCourses)
