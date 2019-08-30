import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)


# python shell, import secrets, secrets.token_hex(16) >>>
app.config['SECRET_KEY'] = 'f9e7c50f4f7870c02924dfdc626f9037'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Shell:
# $ from blog import db
# $ db.create_all()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# 'login' is the name of our login function in routes.py
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('ychnkckmtr@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('#')
mail = Mail(app)

from blog import routes