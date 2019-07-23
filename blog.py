from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# python shell, import secrets, secrets.token_hex(16) >>>
app.config['SECRET_KEY'] = 'f9e7c50f4f7870c02924dfdc626f9037'

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
