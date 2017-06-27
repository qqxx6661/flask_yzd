# -*- coding: utf-8 -*-
from app import db


class Monitor(db.Model):
    __tablename__ = 'monitor'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, nullable=False)
    item_name = db.Column(db.String(128), server_default='')
    item_price = db.Column(db.Float, server_default='')
    user_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    user_id = (db.Integer, db.ForeignKey('user.user_id'))
    mall_id = db.Column(db.Integer, nullable=False)
    note = db.Column(db.String(128), server_default='')
    add_date = db.Column(db.String(64), server_default='')

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<Monitor {}> '.format(self.id)


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64), nullable=False)
    user_pwd = db.Column(db.String(64), nullable=False)
    user_email = db.Column(db.String(64), nullable=False)
    register_date = db.Column(db.String(64), server_default='')

    def __repr__(self):
        return '<User {}>'.format(self.user_id)
