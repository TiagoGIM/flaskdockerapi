import datetime
from extensions import db
import enum


class InvestmentTypeEnum(enum.Enum):
    STOCK = 'stock'
    FIXED_INCOME = 'NotEmployed'
    DEFAULT = 'Default'


class Investment(db.Model):
    __tablename__ = 'investments'

    id = db.Column(db.Integer, primary_key=True)

    investment_type = db.Column(db.Enum(InvestmentTypeEnum), nullable=False,
                                default=InvestmentTypeEnum.DEFAULT.value)
    portfolio_id = db.Column(db.Integer)
    applied_value = db.Column(db.Numeric(12, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    ticker = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'applied_value': str(self.applied_value),
            'quantity': self.quantity,
            'ticker': self.ticker,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class FixedIncome(db.Model):
    __tablename__ = 'fixed_incomes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ticker = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Numeric(12, 2), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    created_date = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)  # Date the record is up to.  Must be on

    def json(self):
        {
            'id': self.id,
            'name': self.name,
            'ticker': self.ticker,
            'due_date': self.due_date
        }
