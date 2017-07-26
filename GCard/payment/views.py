from django.shortcuts import render
from django.views import  generic
from payment.models import Product,Card,PaymentCard

class card(generic.ListView):
    model = Card
class pDetail(generic.DetailView):
    def get_queryset(self):
        return Product.objects.all()
class hView(generic.ListView):
    def get_queryset(self):
        return Product.objects.all()
class pList(generic.DetailView):
    def get_queryset(self):
        return Product.objects.all()
