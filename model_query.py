from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import postDB
import datetime

app = Flask(__name__)
app.config.from_object('myconfig.DevelopmentConfig')
# app.config.from_object('myconfig.ProductionConfig')
db = SQLAlchemy(app)


def createPost(postID, price):
    building = '麗港城'
    address = '麗港城6座4樓E室'
    newPost = postDB(postID, building, address, price)
    db.session.add(newPost)
    db.session.commit()


def queryPosts():
    queryResult = postDB.query.all()
    for post in queryResult:
        print('query: ' + post.postID + " - " + str(post.price))


def deletePost(postID):
    # delete_q = postDB.__table__.delete().where(postDB.postID == postID)
    delete_q = postDB.__table__.delete().where(postDB.postID.like('%'+postID+'%'))
    db.session.execute(delete_q)
    db.session.commit()


def updatePost(postID):
    update_q = postDB.__table__.update().where(
        postDB.postID == postID
    ).values(
        active=False
    )
    db.session.execute(update_q)
    db.session.commit()


postID = 'AKCB123123'
price = 700
createPost(postID, price)
postID = 'AKCC123124'
price = 710
createPost(postID, price)
postID = 'AKCD123125'
price = 720
createPost(postID, price)
postID = 'AKCE123126'
price = 730
createPost(postID, price)

queryPosts()

deletePost('AKCB')

updatePost('AKCC123124')  # update column active to false
