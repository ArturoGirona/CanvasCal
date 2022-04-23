from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class createAccForm(FlaskForm):##Form for creating account to add to db
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=StringField('Password', validators=[DataRequired()])
    password2=StringField('Password2', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Create')

def validate_email(self, email):    #Extra email validation tool to ensure email isn't taken yet!
    user = User.query.filter_by(email=email.data)
    if user is not None:
        raise ValidationError('This username is taken!')