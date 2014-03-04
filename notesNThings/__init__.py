import os

from sys import path
from flask import Flask
from flask import redirect, request
from application.models import users_model
from application.models.notes_model import db
from application.controllers.courses_controller import CoursesController
from application.controllers.notes_controller import NotesController

app = Flask(__name__)

# need to find a way to dynamically find the config file's path
app.config.from_pyfile("/opt/apps/notes-n-things-env/notes-n-things/config/config.py")
db.init_app(app)
with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()

@app.route('/')
def index():
	return redirect('index.html')

@app.route('/login')
def login():
	return 'login'

@app.route('/courses')
def course_index():
	return CoursesController.getAll()

@app.route('/notes')
def note_index():
	return NotesController.getAll()

@app.route('/notes/<name>')
def show_note(name):
	return NotesController.getByName(name)

@app.route('/courses/<name>')
def show_course(name):
	return CoursesController.getByName(name)
