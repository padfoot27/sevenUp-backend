from app import db
import enum

from app.enums.cardNumber import CardNumber
from app.enums.cardType import CardType

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Enum(CardNumber))
    cardType = db.Column(db.Enum(CardType)) 
    
    def __init__(self, number, cardType):
        self.number = number
        self.cardType = cardType

    def __repr__(self):
        return '<Card %r %r>' % self.number, self.cardType

