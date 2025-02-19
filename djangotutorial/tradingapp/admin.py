from django.contrib import admin

from .models import Stock, BuyStock, Buy, Payment, UserProfile

admin.site.register(Stock)
admin.site.register(BuyStock)
admin.site.register(Buy)
admin.site.register(Payment)
admin.site.register(UserProfile)