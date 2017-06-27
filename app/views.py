from app import app
from flask import render_template
from models import User, Monitor


@app.route('/')
def index():
    return render_template("index.html", text="Hello World")


@app.route('/all')
def show_all():
    user = User.query.order_by(User.user_id)
    return render_template('all.html', user=user)
