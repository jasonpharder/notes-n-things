from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:yellow'>I am app 1</span>"
