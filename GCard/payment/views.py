from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from payment.models import Product as ProductModel
from payment.models import Card as CardModel
from payment.models import PaymentCard as PaymentCardModel
from payment.models import Movement as MovementModel
from django.http import Http404
from payment.forms import *
class LoginCreateView(LoginRequiredMixin, generic.CreateView):
    pass

class pDetail(generic.DetailView):
    def get_queryset(self):
        return ProductModel.objects.all()

class hView(generic.ListView):
    model = ProductModel
    template_name = "payment/home.html"


class AddBalance(LoginFormView):
    form_class = AddBalance
    template_name = "payment/card_add_balance_form.html"
    success_url = "/"
    @method_decorator(login_required)
    def post(self, request, *a, **kw):
        return super().post(request, *a, **kw)
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
