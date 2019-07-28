from blog.models import User, Post
from flask import render_template, url_for, flash, redirect
from blog.forms import RegistrationForm, LoginForm
from blog import app


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
       hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       user = User(username=form.username.data, email=form.email.data, password=hash_pw)
       db.session.add(user)
       db.session.commit()
       flash(f'Your account has been created! You are now able to log in.', 'success')
       return redirect(url_for('login'))
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