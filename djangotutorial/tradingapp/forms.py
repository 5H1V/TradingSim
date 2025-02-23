from django import forms
from .models import PortfolioItem

class TradeForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['symbol', 'price', 'shares']
