from django.shortcuts import render
from django.views import generic
from payment.models import *
class card(generic.ListView):
    model = Card
class pDetail(generic.DetailView):
    def get_queryset(self):
        return Product.objects.all()
class hView(generic.ListView):
    model = Product
    template_name = "payment/home.html"

class balance(generic.DetailView):
    template_name =  "payment/addbalance.html"
class HowItWorks(generic.TemplateView):
    template_name = "payment/how_it_works.html"
