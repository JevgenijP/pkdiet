from person import Person
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    p1 = Person("kuku")
    return str(p1.datastructure)

