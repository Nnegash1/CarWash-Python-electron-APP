import sys
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'mysecretkey'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worker.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
admin = Admin(app)
login_manager = LoginManager()
login_manager.init_app(app)

from flaskwash import route