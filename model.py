# from flask import Flask, render_template, url_for, session, request, redirect
# from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import datetime

app = Flask(__name__)
app.config.from_object('myconfig.DevelopmentConfig')
# app.config.from_object('myconfig.ProductionConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class postDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.Text)
    postID = db.Column(db.Text)
    address = db.Column(db.Text)
    price = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    date_added = db.Column(db.Date, default=datetime.datetime.utcnow)

    def __init__(self, postID, building, address, price):
        self.building = building
        self.postID = postID
        self.address = address
        self.price = price


if __name__ == '__main__':
    manager.run()


# python model.py db init    <-- create DB
# python model.py db migrate   <--  create migration
# python model.py db upgrade   <--  commit/update table structure


