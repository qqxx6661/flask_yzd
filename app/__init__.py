# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__) #创建Flask application对象
app.config.from_object('config')
from app import views 