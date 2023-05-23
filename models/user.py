import datetime
from extensions import db
import enum


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    portfolios = db.relationship('Portfolio', backref='user', lazy=True)

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'portfolios': [port.id.json() for port in self.portfolios]
        }


class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    investments = db.relationship('Investment', backref='portfolio', lazy=True)

    def json(self):
        investments_list = []
        for investment in self.investments:
            investments_list.append({
                'id': investment.id,
                'applied_value': str(investment.applied_value),
                'quantity': investment.quantity,
                'ticker': investment.ticker,
                'investment_type': str(investment.investment_type)
            })
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'investments': investments_list
        }


class InvestmentType(enum.Enum):
    STOCK = 'stock'
    FIXED_INCOME = 'NotEmployed'
    DEFAULT = 'Default'


class Investment(db.Model):
    __tablename__ = 'investments'

    id = db.Column(db.Integer, primary_key=True)

    investment_type = db.Column(db.Enum(InvestmentType), nullable=False,
                                default=InvestmentType.DEFAULT.value)

    applied_value = db.Column(db.Numeric(12, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    ticker = db.Column(db.String(255), nullable=False)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)


class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ticker = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Numeric(12, 2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def json(self):
        '''Return a JSON representation of the object'''
        return {'id': id, 'name': self.name, 'ticker': self.ticker, 'price': self.price}


class FixedIncome(db.Model):
    __tablename__ = 'fixed_incomes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ticker = db.Column(db.String(20), nullable=False)
    # Price of the stock.  Must be positive.
    price = db.Column(db.Numeric(12, 2), nullable=False)
    # Date the income is due.  Must be on or after today's
    due_date = db.Column(db.Date, nullable=False)
    # Date the record was created.  Must
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
