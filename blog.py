from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# python shell, import secrets, secrets.token_hex(16) >>>
app.config['SECRET_KEY'] = 'f9e7c50f4f7870c02924dfdc626f9037'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Shell:
# $ from blog import db
# $ db.create_all()
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    image_field = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User: ('{self.username}', '{self.email}', '{self.image_field}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post: ('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author': 'Yucehan Kucukmotor',
        'title': 'First Post',
        'content': 'What does the first post say?',
        'date_posted': 'July 17, 2019'
    },
    {
        'author': 'Emircan Kucukmotor',
        'title': 'Second Post',
        'content': 'What does the second post say?',
        'date_posted': 'July 18, 2019'
    }
]

@app.route('/')         # both routes are feeding the same view functions
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
       flash(f'Account created for {form.username.data}!', 'success')
       return redirect(url_for('home_page'))
   return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login unsuccessful. Please check your username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
