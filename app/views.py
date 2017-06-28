from app import app
from flask import render_template
from models import User, Monitor


@app.route('/')
def to_index():
    return render_template("index.html")


@app.route('/all')
def show_all():
    user = User.query.order_by(User.user_id)
    return render_template('all.html', user=user)


@app.route('/login')
def to_login():
    return render_template('login.html')


@app.route('/monitor')
def to_monitor():
    return render_template('monitor.html', user=user)

