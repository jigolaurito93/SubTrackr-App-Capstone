from flask import Flask

app = Flask(__name__)


# This has to be at the bottom of the file
from app import routes