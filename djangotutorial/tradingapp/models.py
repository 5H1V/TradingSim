from django.db import models
    
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class User(models.Model):
    user_name
    user_ID
    password
    trading_wallet
    stocks_owned

class trading_wallet(models.Model):
    stocks_owned
    password
    
class stocks_owned(models.Model):
    stock
    time data 
    price
    quantity Bought
    transaction ID
    user_ID

class stocks(models.Model):
    price
    name
    ticker
    history
    
class History(models.Model):
    dates
    prices
