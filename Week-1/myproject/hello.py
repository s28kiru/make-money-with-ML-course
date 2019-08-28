from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new_route')
def hello_kiru():
    return 'Hello, Kiru!'