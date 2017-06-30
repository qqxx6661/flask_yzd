# -*- coding: utf-8 -*-
from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from models import User, Monitor, ROLE_USER, ROLE_ADMIN
from forms import LoginForm, SignUpForm, AboutMeForm, AddMonitorItemForm
import datetime
from string import strip


@app.route('/monitor')
def to_monitor():
    return render_template('monitor.html', title='Monitor')


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Home")


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 验证用户是否被验证
    if current_user.is_authenticated:
        return redirect('index')
    # 注册验证
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
                flash("数据库读取错误，请重试")
                return redirect('/login')

            # flash(request.form.get('user_name'))
            # flash('remember me? ' + str(request.form.get('remember_me')))
            return redirect(url_for("index", user_id=current_user.id))
        else:
            flash('没有该用户，请注册')
            return redirect('/login')

    return render_template("login.html", title="Sign In", form=form)



@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
            flash("用户名或邮箱重复")
            return redirect('/sign-up')

        if len(user_name) and len(user_email):
            user.nickname = user_name
            user.email = user_email
            user.role = ROLE_USER
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("数据库报错请重试")
                return redirect('/sign-up')

            flash("登陆成功")
            return redirect('/login')

    return render_template("sign_up.html", form=form)


@app.route('/user/<int:user_id>', methods=["POST", "GET"])
@login_required
def users(user_id):
    form = AboutMeForm()
    user = User.query.filter(User.id == user_id).first()
    if not user:
        flash("The user is not exist.")
        redirect("/index")
    all_item = user.all_item.all()

    return render_template("user.html", form=form, user=user, all_item=all_item)


@app.route('/addmonitoritem/<int:user_id>', methods=["POST", "GET"])
@login_required
def addmonitoritem(user_id):
    form = AddMonitorItemForm()
    item = Monitor()
    if form.validate_on_submit():
        item_id = request.form.get("item_id")
        if not len(strip(item_id)):
            flash("The content is necessray!")
            return redirect(url_for("addmonitoritem", user_id=user_id))
        user_price = request.form.get("user_price")
        if not len(strip(user_price)):
            flash("The content is necessray!")
            return redirect(url_for("addmonitoritem", user_id=user_id))
        mall_id = request.form.get("mall_id")
        if not len(strip(item_id)):
            flash("The content is necessray!")
            return redirect(url_for("addmonitoritem", user_id=user_id))
        item.item_id = item_id
        item.user_price = user_price
        item.mall_id = mall_id
        item.add_date = datetime.datetime.now()
        item.user_id = user_id
        item.status = True

        try:
            db.session.add(item)
            db.session.commit()
        except:
            flash("数据库报错请重试")
            return redirect(url_for("addmonitoritem", user_id=user_id))

        flash("添加商品成功")
        return redirect(url_for("users", user_id=user_id))

    return render_template("addmonitoritem.html", form=form)