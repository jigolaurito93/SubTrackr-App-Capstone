from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm, PostForm
from app.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("landing.html")

@app.route("/")
@login_required
def index():
    form = SignUpForm
    posts = Post.query.all()
    return render_template("index.html", posts=posts, form=form)

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
        return redirect(url_for('index'))
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
            login_user(user)
            flash(f'You have successfully logged in as {username}','success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password Please try again', 'danger')
            return redirect(url_for('login'))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'info')
    return redirect(url_for('index'))


@app.route('/create', methods=["GET", "POST"])
# Login required decorator requires user to be logged in before accessing this route/page
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        print('Horaaaay! You have created a post!')
        subscription = form.subscription.data
        amount = form.amount.data
        date = form.date.data
        frequency = form.frequency.data
        image_url = form.image_url.data # or Non
        print(current_user)
        new_post = Post(subscription=subscription, amount=amount, image_url=image_url, date=date, frequency=frequency, user_id=current_user.id)
        print(subscription, amount, image_url, date, frequency)
        flash(f"{new_post.subscription} Subscription Created Successfully!", "success")
        return redirect(url_for('index'))
    return render_template("create.html", form=form)

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/edit/<post_id>', methods=["GET", "POST"])
# So only logged in users can edit their posts
@login_required
def edit_post(post_id):
    form = PostForm()
    post_to_edit = Post.query.get_or_404(post_id)
    # Make sure that the post author is the current user
    if post_to_edit.author != current_user:
        flash('You do not have permission to edit this post', 'danger')
        return redirect(url_for('index'))
    
    # If form submitted, update Post
    if form.validate_on_submit():
        #  Update the post with the form data
        post_to_edit.subscription = form.subscription.data
        post_to_edit.amount = form.amount.data
        # post_to_edit.date = form.date.data
        post_to_edit.frequency = form.frequency.data
        post_to_edit.image_url = form.image_url.data
        db.session.commit()
        flash(f'{post_to_edit.subscription} subscription has been updated successfully!', "success")
        return redirect(url_for('index'))
    
    # Pre-populate the form with the Post to Edit's values
    form.subscription.data = post_to_edit.subscription
    form.amount.data = post_to_edit.amount
    # form.date.data = post_to_edit.date
    form.frequency.data = post_to_edit.frequency
    form.image_url.data = post_to_edit.image_url
    return render_template("edit.html", form=form, post=post_to_edit)
    
@app.route('/delete/<post_id>', methods=["GET", "POST"])
@login_required
def delete_post(post_id):
    post_to_delete = Post.query.get_or_404(post_id)
    # Make sure that the post author is the current user
    if post_to_delete.author != current_user:
        flash('You do not have permission to delete this post', 'danger')
        return redirect(url_for('index'))
    
    db.session.delete(post_to_delete)
    db.session.commit()
    flash(f'{post_to_delete.subscription} subscription has been deleted successfully!', "success")
    return redirect(url_for('index'))