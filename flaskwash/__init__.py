import sys
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = '_p#&)K.27t-$OANuX/#4&D2Mz:Cb|2'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worker.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATION'] = True



db = SQLAlchemy(app)
admin = Admin(app)
from flaskwash import route