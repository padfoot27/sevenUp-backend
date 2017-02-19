from app import db
from app.shared.deckCard import deckCard
from app.cards.models import Card
from app.game.models import Game
import enum

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deckType = db.Column(db.String(120))
    cards = db.relationship('Card', secondary = deckCard, backref = db.backref('decks', lazy='dynamic'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    
def __init__(self, deckType):
    self.deckType = deckType
