from flask.ext.sqlalchemy import SQLAlchemy
from notesNThings.application.models.stub_database import stubCourses
from notesNThings.application.models.stub_database import stubTests

import json

db = SQLAlchemy()

class Course (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'courses'
    courseID = db.Column(db.Integer, primary_key = True)
    term = db.Column(db.Integer)
    name = db.Column(db.String(9))
    alt_name = db.Column(db.String(255))
    professor = db.Column(db.Integer)

    def __init__(self, courseID, term, name, alt_name, professor):
        self.courseID = courseID
        self.term = term
        self.name = name
        self.alt_name = alt_name
        self.professor = professor

def getAllCourses():
    return json.dumps(stubCourses)