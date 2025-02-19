import random
import string
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from .forms import CheckoutForm, PaymentForm
from .models import UserProfile, Stock, BuyStock, Buy, Payment

def stocks(request):
    context = {
        'stocks': Stock.objects.all()
    }
    return render(request, "stocks.html", context)

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            buy = Buy.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form' : form,
                'buy' : buy
            }
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("tradingapp:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            buy = Buy.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                return redirect('tradingapp:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("tradingapp:order-summary")

class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Buy.objects.get(user=self.request.user, ordered=False)
        context = {
            'order': order,
            'DISPLAY_COUPON_FORM': False,
            'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUBLIC_KEY
        }
        return render(self.request, "payment.html", context)


class HomeView(ListView):
    model = Stock
    paginate_by = 10
    template_name = "home.html"

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            buy = Buy.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': buy
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

class StockDetailView(DetailView):
    model = Stock
    template_name = "stock.html"

def wallet(request):
    return render(request, "wallet.html")

def account(request):
    return render(request, "account.html")
