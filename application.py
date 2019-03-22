from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/notes", methods=["POST"])
def note():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
        return render_template("notes.html", notes=session["notes"])


@app.route("/")
def index():
    headline = "Hello!"
    return render_template("notes.html")


@app.route("/more")
def more():
    return render_template("second.html")


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)


# @app.route("/<string:name>")
# def hello(name):
#     name = name.capitalize()
#     return "Hello".name

@app.route("/new_year")
def new_year():
    new_year = True
    now = datetime.datetime.now()
    new_year = now.year == 1 and now.day == 1
    return render_template("index.html", new_year=new_year)


@app.route("/users")
def users():
    users = ["Alice", "Bob", "Charles"]
    return render_template("index.html", users=users)
