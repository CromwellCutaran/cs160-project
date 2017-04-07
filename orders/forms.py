from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = (
            "first_name",
            "last_name",
            "address",
            "city",
            "zipcode",
          )
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Zipcode'}),

        }