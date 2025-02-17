from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


'''
class User(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    user_id = models.IntegerField(max_length=50, primary_key=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class trading_wallet(models.Model):
    user_id = models.ForeignKey(User, )
    # Edit password to be safer
    trading_password
    stocks_owned
    balance
    updated_balance
    
class stocks_owned(models.Model):
    user_id
    stocks
    avg_price
    quantity_bought
    transaction_id

class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    
    # Many to one relationship
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True, nullable=False)
    user = db.relationship("User", back_populates="transactions")

    company_name = db.Column(db.String(128), index=True)
    company_symbol = db.Column(db.String(128), index=True, nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    trans_type = db.Column(db.String(128), index=True, nullable=False)
    transacted_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

class stocks(models.Model):
    price
    name
    ticker
    history
    
class History(models.Model):
    dates
    prices

'''