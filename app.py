from person import Person
from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get/<user>")
def get_user(user):
     u = Person(user)
     return json.dumps(u.datastructure)

