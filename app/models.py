# -*- coding: utf-8 -*-
from app import db


ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    all_item = db.relationship('Monitor', backref='author', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @classmethod
    def login_check(cls, user_name):
        user = cls.query.filter(db.or_(
            User.nickname == user_name, User.email == user_name)).first()

        if not user:
            return None

        return user

    def __repr__(self):
        return '<User %r>' % self.nickname


class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False)
    item_name = db.Column(db.String(128), default='')
    item_price = db.Column(db.String(64), default='')
    user_price = db.Column(db.String(64), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mall_id = db.Column(db.Integer, nullable=False)
    note = db.Column(db.String(128), default='')
    add_date = db.Column(db.DateTime)

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<Post %r>' % self.id

