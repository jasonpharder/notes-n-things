import os
import flask.ext.restless

from sys import path
from flask import Flask
from flask import redirect, request

from application.models import db

from application.controllers import users_controller
from application.controllers import notes_controller
from application.controllers import courses_controller

from application.models.courses_model import Course
import requests
import json

url = 'http://127.0.0.1/api/users/1'
headers = {'Content-Type': 'application/json'}

app = Flask(__name__)
app.debug = True
# need to find a way to dynamically find the config file's path
app.config.from_pyfile("/opt/apps/notes-n-things/config/config.py")

db.init_app(app)

with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()

# Create the Flask-Restless API manager.
restless_manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

users_controller.create_user_api(restless_manager)
notes_controller.create_note_api(restless_manager)
courses_controller.create_course_api(restless_manager)

@app.route('/')
def index():
	return redirect('index.html')

@app.route('/login')
def login():
	# Make a POST request to create an object in the database.
	#assert response.status_code == 201
	return 'login'