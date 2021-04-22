import sys
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config ['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

from flaskwash import route