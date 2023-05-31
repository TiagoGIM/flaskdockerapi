import datetime
from extensions import db


class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ticker = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Numeric(12, 2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def json(self):
        '''Return a JSON representation of the object'''
        return {
            'id': self.id,
            'name': self.name,
            'ticker': self.ticker,
            'price': self.price,
            'last_updated': self.updated_at.strftime('%Y-%m-%dT%H:%M:%SZ') if self.updated_at else None
        }
