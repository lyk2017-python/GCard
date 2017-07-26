from django.shortcuts import render
from django.views import generic
from payment.models import *
class card(generic.ListView):
    model = Card
class pDetail(generic.DetailView):
    def get_queryset(self):
        return Product.objects.all()
class hView(generic.ListView):
    def get_queryset(self):
        return Product.objects.all()
class balance(generic.DetailView):
    ya = Card
class HowItWorks(generic.TemplateView):
    template_name = "payment/how_it_works.html"
