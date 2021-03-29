from modules import db,login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User_mgmt.query.get(int(user_id))

class User_mgmt(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),nullable=False,unique=True)
    email = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    bg_file = db.Column(db.String(20),nullable=False,default='default_bg.jpg')
    bio = db.Column(db.String(200))
    date = db.Column(db.String(20))
    bday = db.Column(db.String(10))

    posts = db.relationship('Post',backref='author',lazy=True)
    shared = db.relationship('Share',backref='shared',lazy=True)
    bookmarked = db.relationship('Bookmark',backref='saved_by',lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    blop = db.Column(db.String(500),nullable=False)
    stamp = db.Column(db.String(20),nullable=False)
    post_img = db.Column(db.String(20))
    user_id = db.Column(db.Integer,db.ForeignKey('user_mgmt.id'),nullable=False)

    shares = db.relationship('Share',backref='ori_post',lazy=True)
    timeline = db.relationship('Timeline',backref='from_post',lazy=True)
    bookmark = db.relationship('Bookmark',backref='saved_post',lazy=True)

class Share(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    blop_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user_mgmt.id'),nullable=False)
    share_stamp = db.Column(db.String(20),nullable=False)
    share_text = db.Column(db.String(500),nullable=False)

    timeline = db.relationship('Timeline',backref='from_share',lazy=True)

class Timeline(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),default=None)
    share_id = db.Column(db.Integer,db.ForeignKey('share.id'),default=None)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user_mgmt.id'),default=None)