from flask import Flask
from flask import redirect, request
from controlers import notes

app = Flask(__name__)

@app.route('/')
def index():
	return redirect('index.html')

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		#do login stuff here

@app.route('/note/<name>')
def show_notes(name):
	return notes.test(name)

@app.route('/course/<name>')
def show_course(name):
	#courses stuff here
