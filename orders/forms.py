from django import forms
from orders.models import *


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['last_name', 'first_name', 'email', 'address', 'postal_code', 'city']
