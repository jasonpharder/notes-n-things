from sys import path
from flask import Flask
from flask import redirect, request
from application.controllers.courses_controller import CoursesController
from application.controllers.notes_controller import NotesController

app = Flask(__name__)

def init_db():
    """Creates the database tables."""
    #with app.app_context():
    #    db = get_db()
    #    with app.open_resource('schema.sql', mode='r') as f:
    #        db.cursor().executescript(f.read())
    #    db.commit()

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
