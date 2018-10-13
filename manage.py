import os 

from flask_script import Manager
# writing external scripts https://flask-script.readthedocs.io/en/latest/
from flask_migrate import Migrate, MigrateCommand
# https://flask-migrate.readthedocs.io/en/latest/
from app import db, app

from application.models import User

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db',MigrateCommand)

@manager.option('-n', '--config', dest='config', default='development')
def run(config):
    app.run(host="0.0.0.0",port=8080)

@manager.command
def create_table():
    db.create_all()

@manager.command
def drop_table():
    db.drop_all()

@manager.command
def insert_db():
    admin = User(username="admin",password="812323",)
    db.session.add(task)
    db.session.commit()

@manager.option('-n', '--name', dest='name', default='joe')
@manager.option('-u', '--url', dest='url', default=None)
def check(name,url):
    print("{} , {} ".format(name,url))

if __name__ == '__main__':
    manager.run()

