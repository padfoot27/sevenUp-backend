from app import db
from app.deck.models import Deck
from app.shared.userCard import userCard
from app.user.models import User

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activeOnLink = db.Column(db.String(17), nullable=False)
    decks = db.relationship('Deck', backref = 'game', lazy = 'dynamic')
    activeUser_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    activeUser = db.relationship('User', backref = db.backref('game', uselist=False))
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default = db.func.current_timestamp())

    def __init__(activeOnLink):
        self.activeOnLink = activeOnLink
