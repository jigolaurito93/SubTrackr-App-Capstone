from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)



#=============== Login Manager  =================
# Tell the login manager wher to redirect if user is not logged in
login.login_view = 'login'
# It shows a default message when user is not logged in
# To change the default message, do this
login.login_message = "Please log in to access this page"
# It just passes in what category the message should be displayed on the screen
login.login_message_category = 'danger'




# This has to be at the bottom of the file
from app import routes, models