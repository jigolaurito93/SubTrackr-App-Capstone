from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Horaaaay')
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(first_name, last_name, email, username, password)
        flash(f"Thank you {first_name} for signing up!", "success")
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)

@app.route("/login")
def login():
    return render_template("login.html")