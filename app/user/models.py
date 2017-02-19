from app import db
from app.cards.models import Card
from app.shared.userCard import userCard

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    activeOnLink = db.Column(db.String(17), nullable=False)
    cards = db.relationship('Card', secondary=userCard, backref=db.backref('users', lazy = 'dynamic'))
    owner = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default = db.func.current_timestamp())

    def __init__(self, name, activeOnLink):
        self.name = name
        self.activeOnLink = activeOnLink

    def __repr__(self):
        return '<User %r>' % self.name
