from django.db import models
    
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class User(models.Model):
    user_name
    password
    user_id
    trading_wallet

class trading_wallet(models.Model):
    user_id
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
