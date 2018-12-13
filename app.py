from person import Person
from flask import Flask
from flask import render_template
from flask import send_from_directory
import json

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

@app.route("/init.js")
def client():
    return send_from_directory("templates", "init.js")

@app.route("/get/<user>")
def get_user(user):
     u = Person(user)
     return json.dumps(u.datastructure['records'])

