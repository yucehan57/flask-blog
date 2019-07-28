from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                            validators=[DataRequired(), EqualTo('password', 
                            message='Passwords must match')])
    submit = SubmitField('Sign Up')


    
    def validate_username(self, username):
        """Validate username"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'Username {username.data} already exists')

    def validate_email(self, email):
        """Validate email"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'Email {email.data} is taken')

    

class LoginForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')