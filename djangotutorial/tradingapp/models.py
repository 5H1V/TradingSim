from django.db import models
from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    # Edit password to be safer
    password = models.CharField(max_length=50, null=False, blank=False)
    user_id = models.CharField(max_length=50, null=False, blank=False, unique=True)
    trading_wallet

class trading_wallet(models.Model):
    user_id = models.ForeignKey(User, )
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

class stocks(models.Model):
    price
    name
    ticker
    history
    
class History(models.Model):
    dates
    prices
