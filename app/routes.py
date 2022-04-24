from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, createAccForm, updateSetsForm
from app.models import User


# Home page
@app.route('/')
@app.route('/index')
@login_required # Force user to log in before reaching home page
def index():
    return render_template('MainPage.html', title='Home')

# Groups page
@app.route('/groups') # Creates link for groups page
def groups():
    return render_template('GroupsPage.html', title='Groups')

# Settings page
@app.route('/settings', methods=['GET', 'POST']) ##Updating settings route to include form to update settings!
def settings():

    form=updateSetsForm()     # Create Registration form
    if request.method=='GET':
        form.email.data= current_user.email
    elif form.validate_on_submit(): 
        if form.newpass.data=='':                #If no new password entered only update email
            if current_user.check_password(form.oldpass.data):   #still must verify old password matches
                current_user.email=form.email.data
                db.session.commit()
                flash('Settings Updated!')
                return redirect(url_for('settings'))
            else:
                flash('Error Incorrect Current Password!') # Invalid login message
                return redirect(url_for('settings'))
        else:                                   #Otherwise check if oldpassword is correct then update
            if current_user.check_password(form.oldpass.data):
                current_user.email=form.email.data
                current_user.set_password(form.newpass.data)
                db.session.commit()
                flash('Settings Updated!')
                return redirect(url_for('settings'))
            else:                               #If old pass doesn't match display error
                flash('Error Incorrect Current Password!')
                return redirect(url_for('settings'))
    return render_template('SettingsPage.html', title='Settings', form=form)

@app.route('/addEvent') # Add events to calendar
def addEvent():
    return render_template('AddEvents.html', title='AddEvent')

@app.route('/addStudy') # Set up study sessions
def addStudy():
    return render_template('AddStudy.html', title='AddStudy')

@app.route('/signin', methods=['GET', 'POST']) # Sign in to CanvasCal account
def signin():
    user = User.query.all() # Check passed loging information against all users in database

    if not user: # Create a test user if there are no users in the database
        u = User(email='test@gmail.com')
        u.set_password('testing')
        db.session.add(u)
        db.session.commit()
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm() # Check submitted login form info against database
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email address')
            return redirect(url_for('signin'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index')) # Direct user to home page if logged in
    return render_template('SignInPage.html', title='Sign In', form=form)

@app.route('/createAcc', methods=['POST', 'GET'])   ##Updated createAcc route to use createAcc Form and 
def createAcc():                                    ##Accompanying logic is pretty straight forward
    form = createAccForm()                          ##We create form then if validated set user settings
    if form.validate_on_submit():                   ##And then add the new user to the DB
        user=User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('signin'))
    return render_template('CreateAccountPage.html', title='Create Account', form=form)


@app.route('/signout') # Log user out and direct to index page (this will really take them to sign-in page)
def signout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signin2')
def signin2():
    return render_template('SignInPage.html', title="Sign In")