from django import forms
from .models import Card, Customer


# class UserForm(forms.Form):
#     name = forms.CharField()
#     cost = forms.CharField()
#     calls = forms.CharField()
#     sms = forms.CharField()
#     limit_mb = forms.CharField()


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone_number', 'card']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['card'].queryset = Card.objects.filter(active=True)


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'number_card', 'date_of_create', 'pay_limit',  'ccv']


class DeactivateCardForm(forms.Form):
    card = forms.ModelChoiceField(
        queryset=Card.objects.filter(active=True))
