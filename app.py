#coding:utf-8
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:g67108864@127.0.0.1:3306/flask1?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
manager = Manager(app)

# 第一个参数是flask实例，第二个参数SQLAlchemy实例
Migrate(app, db)

#manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令哈哈哈
manager.add_command("db", MigrateCommand)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

class Food(UserMixin, db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    addcol = db.Column(db.String(64))
    addcol1 = db.Column(db.String(64))
    addcol2 = db.Column(db.String(64))
# db.create_all()

@app.route("/")
def index():
    return "index"

if __name__ == '__main__':
    manager.run()