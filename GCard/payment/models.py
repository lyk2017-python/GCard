# General Desc of Models -> https://github.com/lyk2017-django/GCard/wiki/Models#gcard-models-description
from django.db import models
from django.conf import settings
import uuid

# Card Digit Generator -> https://github.com/lyk2017-django/GCard/wiki/Models#card_digit_gen-function
def card_digit_gen ():
    return uuid.uuid4().hex[:8]

# Card Model -> https://github.com/lyk2017-django/GCard/wiki/Models#card-model
class Card(models.Model):
     digits = models.CharField(max_length=8, default=card_digit_gen, unique=True)
     balance = models.PositiveSmallIntegerField(default=0)
     # Product Model -> https://github.com/lyk2017-django/GCard/wiki/Models#cards-str
     def __str__(self):
        return "Card No: {no} \n Card Balance: {balance}".format(no=self.digits, balance=self.balance)
# Product Model -> https://github.com/lyk2017-django/GCard/wiki/Models#product-model
class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    image = models.URLField(default="http://lorempixel.com/600/400/sports/")
    def __str__(self):
        return "PK: {pk} \n Title: {title} \n Description: {desc} \n Price: {price} \n Image Url: {im}".format(title=self.title, desc=self.desc, price=self.price, im=self.image, pk=self.pk)
# Payment Card Digit Generator ->  https://github.com/lyk2017-django/GCard/wiki/Models#card_digit_gen-function-1
def paymentcard_digit_gen():
    return uuid.uuid4().hex[:10]

# Payment Card Model -> https://github.com/lyk2017-django/GCard/wiki/Models#card-model-1
class PaymentCard(models.Model):
    digits = models.CharField(max_length=10, default=paymentcard_digit_gen, unique=True)
    balance = models.PositiveSmallIntegerField(default=0)
    used = models.BooleanField(default=False)
    def __str__(self):
        return "Card No: {dig} \n Card Balance: {bal} \n Is Card Used: {used} ".format(dig=self.digits, bal=self.balance, used=self.used)
