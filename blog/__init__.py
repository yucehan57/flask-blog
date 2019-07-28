from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# python shell, import secrets, secrets.token_hex(16) >>>
app.config['SECRET_KEY'] = 'f9e7c50f4f7870c02924dfdc626f9037'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Shell:
# $ from blog import db
# $ db.create_all()
db = SQLAlchemy(app)

from blog import routes