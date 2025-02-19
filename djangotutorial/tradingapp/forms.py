from django import forms

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    payment_option = forms.ChoiceField(
    widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class PaymentForm(forms.Form):
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)