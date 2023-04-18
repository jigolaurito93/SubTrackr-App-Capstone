from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy(app)

migrate = Migrate(app, db)

# This has to be at the bottom of the file
from app import routes, models