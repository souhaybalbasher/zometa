from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pass@word'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
STATIC_URL = '/static'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'

from modules import routes
db.create_all()