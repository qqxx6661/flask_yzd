#-*- coding:utf-8 -*-
import datetime
from string import strip

from flask import (
    render_template, flash, redirect, session, url_for, request, g)
from flask.ext.login import (
    login_user, logout_user, current_user, login_required)
from forms import (
    LoginForm, SignUpForm, AboutMeForm, PublishBlogForm)
from models import (
    User, Post, ROLE_USER, ROLE_ADMIN)
from utils import PER_PAGE
from app import app, db, lm


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/index')
def index():
    user = 'Man'
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(
        "index.html",
        title="Home",
        user=user,
        posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect('index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'))
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/login')
            flash('Your name: ' + request.form.get('user_name'))
            flash('remember me? ' + str(request.form.get('remember_me')))
            return redirect(url_for("users", user_id=current_user.id))
        else:
            flash('Login failed, Your name is not exist!')
            return redirect('/login')
    return render_template(
        "login.html",
        title="Sign In",
        form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    user = User()
    if form.validate_on_submit():
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')
        register_check = User.query.filter(db.or_(
            User.nickname == user_name, User.email == user_email)).first()
        if register_check:
            flash("error: The user's name or email already exists!")
            return redirect('/sign-up')
        if len(user_name) and len(user_email):
            user.nickname = user_name
            user.email = user_email
            user.role = ROLE_USER
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/sign-up')
            flash("Sign up successful!")
            return redirect('/index')
    return render_template(
        "sign_up.html",
        form=form)

@app.route('/user/<int:user_id>', defaults={'page':1}, methods=["POST", "GET"])
@app.route('/user/<int:user_id>/page/<int:page>', methods=['GET', 'POST'])
@login_required
def users(user_id, page):
    form = AboutMeForm()
    if user_id != current_user.id:
        flash("Sorry, you can only view your profile!", "error")
        return redirect("/index")
    # pagination = user.posts.paginate(page, PER_PAGE, False).items
    pagination = Post.query.filter_by(
        user_id = current_user.id
        ).order_by(
        db.desc(Post.timestamp)
        ).paginate(page, PER_PAGE, False)
    return render_template(
        "user.html",
        form=form,
        pagination=pagination)


@app.route('/publish/<int:user_id>', methods=["POST", "GET"])
@login_required
def publish(user_id):
    form = PublishBlogForm()
    posts = Post()
    if form.validate_on_submit():
        blog_body = request.form.get("body")
        if not len(strip(blog_body)):
            flash("The content is necessray!")
            return redirect(url_for("publish", user_id=user_id))
        posts.body = blog_body
        posts.timestamp = datetime.datetime.now()
        posts.user_id = user_id
        try:
            db.session.add(posts)
            db.session.commit()
        except:
            flash("Database error!")
            return redirect(url_for("publish", user_id=user_id))
        flash("Publish Successful!", "success")
        return redirect(url_for("publish", user_id=user_id))
    return render_template(
        "publish.html",
        form=form)

@app.route('/user/about-me/<int:user_id>', methods=["POST", "GET"])
@login_required
def about_me(user_id):
    user = User.query.filter(User.id == user_id).first()
    if request.method == "POST":
        content = request.form.get("describe")
        if len(content) and len(content) <= 140:
            user.about_me = content
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("Database error!")
                return redirect(url_for("users", user_id=user_id))
        else:
            flash("Sorry, May be your data have some error.")
    return redirect(url_for("users", user_id=user_id))