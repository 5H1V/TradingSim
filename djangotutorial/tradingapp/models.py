from django.db import models

# Stock
# Time data 
# Price
# Quantity Bought
# Transaction ID
# User ID
    
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
