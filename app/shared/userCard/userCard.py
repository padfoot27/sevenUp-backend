from app import db
from app.cards.models import Card
from app.user.models import User

userCard = db.Table('userCard', 
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('card_id', db.Integer, db.ForeignKey('card.id')))
