from app import db

class Cryptocurrency(db.Model):
    __tablename__ = 'cryptocurrencies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    market_cap = db.Column(db.Float)
    volume = db.Column(db.Float)
    logo_url = db.Column(db.String(255))

class CryptoPrice(db.Model):
    __tablename__ = 'crypto_prices'
    id = db.Column(db.Integer, primary_key=True)
    crypto_id = db.Column(db.Integer, db.ForeignKey('cryptocurrencies.id'), nullable=False)
    crypto = db.relationship('Cryptocurrency', backref='prices')
    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    open = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)