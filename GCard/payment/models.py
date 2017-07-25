from django.db import models
from django.conf import settings
import uuid

def card_digit_gen ():
    return uuid.uuid4().hex[:8]

class Card(models.Model):
     digits = models.CharField(max_length=8, default=card_digit_gen, unique=True)
     balance = models.PositiveSmallIntegerField(default=0)
     def __str__(self):
        return "Card No: {no} \n Card Balance: {balance}".format(no=self.digits, balance=self.balance)

class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    image = models.URLField()
    def __str__(self):
        return "Title: {title} \n Description: {desc} \n Price: {price} \n Image Url: {im}".format(title=self.title, desc=self.desc, price=self.price, im=self.image)
def paymentcard_digit_gen():
    return uuid.uuid4().hex[:10]

class PaymentCard(models.Model):
    digits = models.CharField(max_length=10, default=paymentcard_digit_gen, unique=True)
    balance = models.PositiveSmallIntegerField(default=0)
    used = models.BooleanField(default=False)
    def __str__(self):
        return "Card No: {dig} \n Card Balance: {bal} \n Is Card Used: {used} ".format(dig=self.digits, bal=self.balance, used=self.used)
