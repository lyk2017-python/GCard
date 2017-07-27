from django.contrib import admin
from payment.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['digits', 'balance']

@admin.register(PaymentCard)
class PaymentCardAdmin(admin.ModelAdmin):
    list_display = ['digits', 'balance', 'used']

