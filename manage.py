# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from app import app, db
from app.models import User, Monitor

manager = Manager(app)

manager.add_command("runserver",
                    Server(host='127.0.0.1', port=5000, use_debugger=True))


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Monitor=Monitor)


if __name__ == '__main__':
    manager.run()

