from django.db.models.signals import post_save
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.shortcuts import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Stock(models.Model):
    stock_name = models.CharField(max_length=100)
    price = models.FloatField()
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.stock_name

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart")

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart")

class BuyStock(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.stock.stock_name}"

    def get_final_price(self):
        return self.quantity * self.stock.price

class Buy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    
    stocks = models.ManyToManyField(BuyStock)
    
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_stock in self.stocks.all():
            total += order_stock.get_final_price()

        return total

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

'''
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