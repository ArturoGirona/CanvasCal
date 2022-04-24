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
    password=PasswordField('Password', validators=[DataRequired()])
    password2=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Create Account')
    def validate_email(self, email):    #Extra email validation tool to ensure email isn't taken yet!
        user = User.query.filter_by(email=email.data).scalar() #Note validate_email must be in createAcc class
        if user is not None:
            raise ValidationError('This email is already in use!')

        
class updateSetsForm(FlaskForm):##Form for updating settings on settings page!
    email=StringField('Email', validators=[DataRequired(), Email()]) # Email address
    oldpass=StringField('Old Password', validators=[DataRequired()]) # Old password
    newpass=StringField('New Password') # New password
    newpass2=StringField('Confirm New Password', validators=[EqualTo('newpass')]) # Re-type new password
    submit=SubmitField('Update Account Settings') # Submit button