from django.shortcuts import render
from django.views import  generic
from payment.models import Product,Card,PaymentCard


class HomeView(generic.ListView):


class ProductView(generic.ListView):


class ProductView(generic.DetailView):
