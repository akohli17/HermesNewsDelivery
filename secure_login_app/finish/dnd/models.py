from flask_login import UserMixin

from dnd import db

# User database tables with respective fields
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=True)
    last_name = db.Column(db.String(50), unique=True)
    date_of_birth = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"

class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interest = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='interestOfUser', lazy=True)

    def __repr__(self):
        return f"Interest('{self.interest}', '{self.user.username}')"

class Article(db.Model):
    id = db.Column(db.String(1000), nullable=False, primary_key=True)
    t = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='articleOfUser', lazy=True)
    isBookmark = db.Column(db.Boolean, nullable=False, default=False)
    interest = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Article('{self.id}', '{self.t}', '{self.user.username}', '{self.interest}')"