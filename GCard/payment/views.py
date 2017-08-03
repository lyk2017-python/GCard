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

class ts(generic.DetailView):
    def get_context_data(self, **kwargs):
        context = super(ts, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            query = Movement.objects.filter(movement_card=self.request.user.card)
            if query.exists:
                context['transactions'] = query.all()
            else:
                context['transactions'] = "There Are No Transactions"
        return context
    model = Movement
    template_name = "payment/ts.html"

class pDetail(generic.DetailView):
    def get_queryset(self):
        return ProductModel.objects.all()

class hView(generic.ListView):
    def get_context_data(self, **kwargs):
        context = super(hView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            qr = CardModel.objects.filter(user=self.request.user)
            context['balance'] = qr.first()
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
class RegistrationView(generic.FormView):
    form_class = CustomUserCreationForm
    template_name = "payment/signup.html"
    success_url = "/"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
