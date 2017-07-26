from django.conf.urls import url
from payment.views import HomeView, ProductView

urlpatterns = [
    url(r"^$", HomeView, name="home"),
    url(r"^product/(?P/<slug>[A-Za-z0-9\-]+)$",ProductView),
    url(r"^detail/(?P<pk>\d+)-(?P/<slug>[A-Za-z0-9\-]+)$",ProductDetail, name="product_detail"),

