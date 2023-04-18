from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

# This has to be at the bottom of the file
from app import routes