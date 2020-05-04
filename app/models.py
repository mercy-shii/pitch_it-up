from flask_login import UserMixin
#from .import login_manager
from . import db

#@login_manager.user_loader
#def load_user(user_id):
    #return User.query.get(int(user_id))

class User (db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.string(255))
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitches',backref = 'author',lazy = 'dynamic')
    comments = db.relationship('Comments',backref = 'author',lazy = 'dynamic')
    




    def __repr__(self):
        return f'User {self.username}'

class Pitches (db.Model):
    """ Pitches model """

    __tablename__ = "pitches"
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255),index = True)
    pitch = db.Column(db.String(255),unique = True,index = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comments',backref = 'title',lazy ='dynamic')



    def __repr__(self):
        return f'Pitches {self.pitch}'

class Comments (db.Model):
    """ Comments model """

    __tablename__ = "comments"
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255),index = True)
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))



    



    

