from django import forms
from payment.models import *

class AddBalance(forms.ModelForm):
    model = Card
    exclude = ['id']
    exclude = ['balance']
x = AddBalance(request.POST)
x.is_valid()
x.save()

x.as_p
