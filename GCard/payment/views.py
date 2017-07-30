from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from payment.models import Product as ProductModel
from payment.models import Card as CardModel
from payment.models import PaymentCard as PaymentCardModel
from payment.models import Movement as MovementModel
from django.http import Http404
from payment.forms import *

class pDetail(generic.DetailView):
    def get_queryset(self):
        return ProductModel.objects.all()

class hView(generic.ListView):
    model = ProductModel
    template_name = "payment/home.html"


class AddBalance(generic.FormView):
    form_class = AddBalance
    template_name = "payment/card_add_balance_form.html"
    success_url = "/"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
class Card(generic.DetailView):
    model = CardModel
    template_name = "payment/card.html"
    def get_queryset(self):
        return CardModel.objects.all()
class HowItWorks(generic.TemplateView):
    template_name = "payment/how_it_works.html"
class cardform(generic.TemplateView):
    template_name = "payment/id.html"
