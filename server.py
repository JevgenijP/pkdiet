from person import Person
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    p1 = Person("kuku")
    return render_template('index.html', name = p1.datastructure['user_data']['user'])

