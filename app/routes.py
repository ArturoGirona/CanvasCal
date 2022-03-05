from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Arturo'}
    return render_template('MainPage.html', title='Home', user=user)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html', title='Calendar')

@app.route('/todolist')
def tasklist():
    return render_template('todolist.html', title='Todo List')
