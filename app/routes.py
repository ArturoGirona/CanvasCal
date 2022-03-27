from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Arturo'}
    return render_template('MainPage.html', title='Home', user=user)

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

@app.route('/signin')
def signin():
    return render_template('SignInPage.html', title='Sign In')