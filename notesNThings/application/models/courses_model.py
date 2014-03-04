from flask.ext.sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class Course (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'courses'
    courseID = db.Column(db.Integer, primary_key = True)
    term = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(64), unique=True)
    alt_name = db.Column(db.String())
    professor = db.Column()

    def __init__(self, courseID, term, name, alt_name, professor):
        self.courseID = courseID
        self.term = term
        self.name = name
        self.alt_name = alt_name
        self.professor = professor

def getAllCourses():
    courses = Course.query.all()
    jsonTest = "{'test': { "
    print jsonTest
    for t in courses:
       jsonTest = jsonTest + json.dumps(t.username)
    return jsonTest