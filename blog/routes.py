from flask import render_template, url_for, flash, redirect, \
                  request
from blog.forms import RegistrationForm, LoginForm
from blog import app, db, bcrypt
from blog.models import User, Post
from flask_login import login_user, logout_user, current_user, \
                        login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        # check if user exists
        user = User.query.filter_by(email=form.email.data).first()
        # if user exists check if password input in DB and form matches
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home_page'))
        else:    
            flash('Login unsuccessful. Please check your email and password', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home_page'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')