from django import forms
from django.db import transaction,models
from payment.models import Card as CardModel
from payment.models import PaymentCard as PaymentCardModel
from payment.models import Movement as MovementModel
from payment.models import Product as ProductModel
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
class Buy(forms.Form):
    card_digits = forms.CharField(max_length=8, min_length=8)
    product_pk = forms.IntegerField(widget=forms.HiddenInput)
    def clean_card_digits(self):
        x = self.data.get("card_digits")
        qs = CardModel.objects.filter(digits=x)
        if qs.exists():
            return qs.first()
        else:
            raise forms.ValidationError("Wrong Main Card ID")
    def clean_product_pk(self):
        y = self.data.get("product_pk")
        print(y)
        qy = ProductModel.objects.filter(pk=y)
        print(qy)
        if qy.exists():
            return qy.first()
        else:
            raise forms.ValidationError("Wrong Product ID")
    def save(self):
        cd = self.cleaned_data["card_digits"]
        product = self.cleaned_data["product_pk"]
        with transaction.atomic():
            cd.balance = models.F("balance") - product.price
            cd.save(update_fields=["balance"])
            transdesc = "You Bought {product} with {number}".format(product=product.title, number=self.cleaned_data["card_digits"])
            MovementModel.objects.create(movement_desc=transdesc, movement_type=False, movement_amount=product.price, movement_card=cd)
        return product, cd
class AddBalance(forms.Form):
    card_digits = forms.CharField(max_length=8, min_length=8)
    precard_digits = forms.CharField(max_length=10, min_length=10)

    def clean_card_digits(self):
        x = self.data.get("card_digits")
        qs = CardModel.objects.filter(digits=x)
        if qs.exists():
            return qs.first()
        else:
            raise forms.ValidationError("Wrong Main Card ID")

    def clean_precard_digits(self):
        x = self.data.get("precard_digits")
        qs = PaymentCardModel.objects.filter(digits=x, used=False)
        if qs.exists():
            return qs.first()
        else:
            raise forms.ValidationError("Used & Wrong Disposable Card ID")

    def save(self):
        cd = self.cleaned_data["card_digits"]
        pcd = self.cleaned_data["precard_digits"]
        slug = self.cleaned_data["card_digits"]
        with transaction.atomic():
            cd.balance = models.F("balance") + pcd.balance
            cd.save(update_fields=["balance"])
            pcd.used = True
            pcd.save(update_fields=["used"])
            transdesc = "{number} named main card charged by {number2} named pre-paid card".format(number=self.cleaned_data["card_digits"], number2=self.cleaned_data["precard_digits"])
            MovementModel.objects.create(movement_desc=transdesc, movement_type=True, movement_amount=pcd.balance, movement_card=cd)
        return cd, pcd
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
    def save(self, commit=True):
        with transaction.atomic():
            user = super().save(commit=True)
            CardModel.objects.create(user=user)
            #MovementModel.objects.create(movement_user=user)
        return user
class Card(forms.ModelForm):
    model = CardModel
    exclude = ['id', 'balance']

class CardData(forms.Form):
    digits = forms.CharField(min_length=8)
    def clean_digits(self):
        x = self.data.get("digits")
        qs = CardModel.objects.filter(digits=x)
        if qs.exists():
            return qs.first()
        else:
            raise forms.ValidationError("Wrong Main Card ID")
    def gonder(self):
        cd = self.cleaned_data["digits"]
        return cd
