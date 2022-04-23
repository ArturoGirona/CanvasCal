from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, createAccForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('MainPage.html', title='Home')

'''
@app.route('/calendar')
def calendar():
    return render_template('calendar.html', title='Calendar')

@app.route('/todolist')
def tasklist():
    return render_template('todolist.html', title='Todo List')
'''

@app.route('/groups')
def groups():
    return render_template('GroupsPage.html', title='Groups')

@app.route('/settings')
def settings():
    return render_template('SettingsPage.html', title='Settings')

@app.route('/addEvent')
def addEvent():
    return render_template('AddEvents.html', title='AddEvent')

@app.route('/addStudy')
def addStudy():
    return render_template('AddStudy.html', title='AddStudy')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    user = User.query.all()
    if not user:
        u = User(email='test@gmail.com')
        u.set_password('testing')
        db.session.add(u)
        db.session.commit()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email address')
            return redirect(url_for('signin'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('SignInPage.html', title='Sign In', form=form)

@app.route('/createAcc', methods=['POST', 'GET'])   ##Updated createAcc route to use createAcc Form and 
def createAcc():                                    ##Accompanying logic
    flash('Test')
    form = createAccForm()
    if form.validate_on_submit():
        user=User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('signin'))
    return render_template('CreateAccountPage.html', title='Create Account', form=form)


@app.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signin2')
def signin2():
    return render_template('SignInPage.html', title="Sign In")