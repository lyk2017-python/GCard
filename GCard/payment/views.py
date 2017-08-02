from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from payment.models import Product as ProductModel
from payment.models import Card as CardModel
from payment.models import PaymentCard as PaymentCardModel
from payment.models import Movement
from payment.forms import *

class LoginFormView(LoginRequiredMixin, generic.FormView):
    pass

class pDetail(generic.DetailView):
    def get_queryset(self):
        return ProductModel.objects.all()

class hView(generic.ListView):
    def get_context_data(self, **kwargs):
        context = super(hView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['balance'] = self.request.user.card
        return context
    model = ProductModel
    template_name = "payment/home.html"


class AddBalance(LoginFormView):
    form_class = AddBalance
    template_name = "payment/card_add_balance_form.html"
    success_url = "/"
    def get_initial(self):
        initial = super().get_initial()
        initial['card_digits'] = self.request.user.card.digits
        return initial
    def post(self, request, *a, **kw):
        return super().post(request, *a, **kw)
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
class BuyProduct(LoginFormView):
    form_class = Buy
    template_name = "payment/buy.html"
    success_url = "/"
    def get_initial(self):
         initial = super().get_initial()
         initial['card_digits'] = self.request.user.card.digits
         return initial
    @method_decorator(login_required)
    def post(self, request, *a, **kw):
        return super().post(request, *a, **kw)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST"]:
            yeni_data = kwargs["data"].copy()
            yeni_data["product_pk"] = self.kwargs["pk"]
            kwargs["data"] = yeni_data
        return kwargs
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
class Card(generic.DetailView):
    model = CardModel
    template_name = "payment/card.html"
    def get_object(self):
        return self.request.user.CardModel()
class HowItWorks(generic.TemplateView):
    template_name = "payment/how_it_works.html"
class cardform(generic.TemplateView):
    template_name = "payment/id.html"
class RegistrationView(generic.FormView):
    form_class = CustomUserCreationForm
    template_name = "payment/signup.html"
    success_url = "/"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
