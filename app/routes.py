from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm
from app.models import User

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
        check_user = db.session.execute(db.select(User).filter((User.username == username) | (User.email == email))).scalars().all()
        if check_user:
            flash("A user with that username or email already exists", "warning")
            return redirect(url_for('signup'))
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        flash(f"Thank you {new_user.username} for signing up! You can now log in", "success")
        return redirect(url_for('hello'))
    return render_template("signup.html", form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Horaaaay! You are now logged in!')
        username = form.username.data
        password = form.password.data
        print(username, password)
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            flash(f'You have successfully logged in as {username}','success')
            return redirect(url_for('hello'))
        else:
            flash('Invalid username and/or password Please try again', 'danger')
            return redirect(url_for('login'))
    return render_template("login.html", form=form)