from django.contrib import admin
from payment.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'brand',
        'price'
    ]

    search_fields = [
        'title',
        'brand',
        'desc',
        'price'
    ]

    list_filter = ['brand', 'price']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = [
        'digits',
        'balance'
    ]

    search_fields = ['digits']
    list_filter = ['balance']

@admin.register(PaymentCard)
class PaymentCardAdmin(admin.ModelAdmin):
    list_display = [
        'digits',
        'balance',
        'used',
    ]

    search_fields = [
        'digits',
        'used'
    ]

    list_filter = [
        'balance',
        'used'
    ]

    fieldsets = []
