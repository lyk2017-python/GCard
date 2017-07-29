from django.shortcuts import render
from django.views import generic
from django.views.generic import UpdateView
from payment.models import *
from django.http import Http404
from payment.forms import *


class card(generic.ListView):
    model = Card


class pDetail(generic.DetailView):
    def get_queryset(self):
        return Product.objects.all()


class hView(generic.ListView):
    model = Product
    template_name = "payment/home.html"


class AddBalance(generic.FormView):
    form_class = AddBalance
    template_name = "payment/card_add_balance_form.html"
    success_url = "."

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class HowItWorks(generic.TemplateView):
    template_name = "payment/how_it_works.html"
