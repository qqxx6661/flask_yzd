# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

# flask
app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

# flask-Login
lm = LoginManager()
lm.init_app(app)

from app import views, models, db
from models import User, Monitor


# flask-Admin
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 1

admin = Admin(app)
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Monitor, db.session))
