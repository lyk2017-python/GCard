from django.contrib import admin

# Register your models here.
from payment.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass

@admin.register(PaymentCard)
class PaymentCardAdmin(admin.ModelAdmin):
    pass
