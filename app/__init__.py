# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) #创建Flask application对象
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models