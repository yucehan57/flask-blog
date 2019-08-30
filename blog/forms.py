from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, \
                    SubmitField, BooleanField, \
                    TextAreaField
from wtforms.validators import DataRequired, Length, \
                    Email, EqualTo, ValidationError
from .models import User


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



class UserUpdateForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Confirm')


    def validate_username(self, username):
        if username.data != current_user.username:
            """Validate username"""
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(f'Username {username.data} already exists')

    def validate_email(self, email):
        if email.data != current_user.email:
            """Validate email"""
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(f'Email {email.data} is taken')



class PostForm(FlaskForm):
    title = StringField('Title', 
                        validators=[DataRequired(), Length(min=6, max=45)])
    content = TextAreaField('Content', 
                        validators=[DataRequired(), Length(min=15)])
    submit = SubmitField('Post')



class RequestResetForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(f'No account found for that email')



class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                            validators=[DataRequired(), EqualTo('password', 
                            message='Passwords must match')])
    submit = SubmitField('Reset Password')
