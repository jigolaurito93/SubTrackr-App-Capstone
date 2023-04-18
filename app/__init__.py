from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

# This has to be at the bottom of the file
from app import routes, models