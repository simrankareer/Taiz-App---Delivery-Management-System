# forms.py
from django import forms
from .models import Delivery,Shop, ordermodel,product,customer

class OrderForm(forms.ModelForm):
    order = forms.ModelChoiceField(
        queryset=ordermodel.objects.all(),
        to_field_name='id',
        label='Select an Order'
    )

    class Meta:
        model = Delivery
        fields = ['deliverystatus', 'paymentstatus', 'paymentmethod', 'deliveryagent','billamount']

class PlaceOrderForm(forms.Form):
    customer = forms.ModelChoiceField(
        queryset=customer.objects.all(),
        label='Select a Customer'
    )
    
    shop = forms.ModelChoiceField(
        queryset=Shop.objects.all(),
        label='Select a Shop'
    )

    product = forms.ModelMultipleChoiceField(
        queryset=product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Products'
    )

