from backends import  db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column('firstname', db.String, nullable=False)
    lastname = db.Column('lastname', db.String, nullable=False)
    username = db.Column('username', db.String, nullable=False, unique=True)
    email = db.Column('email', db.String, nullable=False)
    password = db.Column('password', db.String, nullable=False)
    
    # address = db.Column('address', db.String(50))
    # usertype = db.relationship('UserType', backref='usertype', lazy=True)


    def __repr__(self):
        return f'{self.username}'

# class UserType(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     userypes = db.Column('usertype', db.String(50), nullable=False)
#     userid = db.Column('userid', db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f'<UserType: {self.usertypes}>'