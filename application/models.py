from app import db, flask_bcrypt
from sqlalchemy.sql import expression

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(255))
    is_authenticated = db.Column(db.Boolean, default=False, server_default="true")
    is_active = db.Column(db.Boolean, default=False, server_default="true")
    is_anonymous = db.Column(db.Boolean, default=False, server_default="true")
    def __repr__(self):
        return "<User %r>"%self.username
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)
    def set_password(self, password):
        return flask_bcrypt.generate_password_hash(password)
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password, password)
    def get_id(self):
        return self.id
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
'''
Simple Example => 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
## ont to Many =>

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')



class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)
## Many to Many => 

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)

'''