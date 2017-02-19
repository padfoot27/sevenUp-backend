from app import db
from app.cards.models import Card
from app.deck.models import Deck

deckCard = db.Table('deckCard', 
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('deck_id', db.Integer, db.ForeignKey('deck.id')))
