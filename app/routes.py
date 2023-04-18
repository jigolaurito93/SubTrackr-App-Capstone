from app import app
from flask import render_template
from app.forms import SignUpForm

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/signup")
def signup():
    form = SignUpForm()

    return render_template("signup.html", form=form)

@app.route("/login")
def login():
    return render_template("login.html")