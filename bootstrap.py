from flask import Flask
from flask import redirect, request

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
	#notes stuff here

@app.route('/course/<name>')
def show_course(name):
	#courses stuff here