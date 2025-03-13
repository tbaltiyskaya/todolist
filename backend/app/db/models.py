from .database import db
from sqlalchemy import Time


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.name}', '{self.email}')"
    

class Password(db.Model):
    __tablename__ = 'passwords'

    id = db.Column(db.BigInteger, db.ForeignKey('users.id'), primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Password('{self.id}','{self.password}')"
    

class List(db.Model):
    __tablename__ = 'lists'
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    author = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    name = db.Column(db.String(80), nullable=False)
    datetype = db.Column(db.Boolean)
    grouptype = db.Column(db.Boolean)

    def __repr__(self):
        return f"List('{self.id}', '{self.author}', '{self.name}', '{self.datetype}', '{self.grouptype}')"
    

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    list = db.Column(db.BigInteger, db.ForeignKey('lists.id'))
    author = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    executor = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(), nullable=True)
    date = db.Column(db.Date, nullable=True)
    time = db.Column(Time, nullable=True)
    priority = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (f"Task('{self.id}', '{self.list}', '{self.author}', '{self.executor}', "
                f"'{self.name}', '{self.desc}', '{self.date}', '{self.time}', "
                f"'{self.priority}', '{self.status}')")


class Access(db.Model):
    __tablename__ = 'accesses'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    list = db.Column(db.BigInteger, db.ForeignKey('lists.id'), nullable=False)
    author = db.Column(db.BigInteger, nullable=False)
    user = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return (f"Access('{self.id}', '{self.list}', '{self.author}', '{self.user}')")
    

class Friend(db.Model):
    __tablename__ = 'friends'
    friend_1 = db.Column(db.BigInteger, db.ForeignKey('users.id'), primary_key=True)
    friend_2 = db.Column(db.BigInteger, db.ForeignKey('users.id'), primary_key=True)

    def __repr__(self):
        return (f"Friend('{self.friend_1}', '{self.friend_2}'")
    


class FriendNotice(db.Model):
    __tablename__ = 'friend_notices'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    sender = db.Column(db.BigInteger, nullable=False)
    getter = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return (f"FriendNotice('{self.id}', '{self.sender}', '{self.getter}'")
    

class ListNotice(db.Model):
    __tablename__ = 'list_notices'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    sender = db.Column(db.BigInteger, nullable=False)
    getter = db.Column(db.BigInteger, nullable=False)
    list = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return (f"FriendNotice('{self.id}', '{self.sender}', '{self.getter}', '{self.list}'")
    



