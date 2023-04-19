from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)
    
    @login.user_loader
    def get_a_user_by_id(user_id):
        return db.session.get(User, user_id)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription = db.Column(db.String(100), nullable=False)
    other = db.Column(db.String(50), nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    # image_url = db.Column(db.String(100), nullable=False, default=random_photos_url)
    date = db.Column(db.String(20), nullable=False)
    frequency = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # SQL - FOREIGN KEY(user_id) REFERENCES user(id)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Post {self.id}|{self.subscription}>"
