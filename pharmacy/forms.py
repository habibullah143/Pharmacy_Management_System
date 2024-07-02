from django import forms
from .models import Medicine, Order

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'price', 'stock']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['medicine', 'quantity']
