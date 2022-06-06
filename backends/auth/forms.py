from flask_wtf import FlaskForm
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=3, max=10)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=10)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=10)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    # usertypes = StringField('Usertype', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),  Length(min=6, max=15)])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message ='Passwords must match') ])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=10)])
    password = PasswordField('Password', validators=[DataRequired(),  Length(min=6, max=15)])
    submit = SubmitField('Login')