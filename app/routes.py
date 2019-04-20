from flask import render_template, flash
from app import app
from app.models import Users

@app.route('/')
def index():
    users_list = Users.query.all()
    return render_template('index.html', title='Users Table', users =users_list)
