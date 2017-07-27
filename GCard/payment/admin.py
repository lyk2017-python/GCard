from django.contrib import admin
from payment.models import *

class ProductAdmin(admin.ModelAdmin):
    pass
class CardAdmin(admin.ModelAdmin):
    pass
class PaymentCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(PaymentCard, PaymentCardAdmin)
