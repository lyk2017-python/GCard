from django.conf.urls import url
from payment.views import *

urlpatterns = [
    url(r"^$", hView.as_view(), name="home"),
    url(r"^detail/(?P<pk>\d+)/$", pDetail.as_view(), name="product_detail"),
    url(r"^transaction/(?P<pk>\d+)/$", ts.as_view(), name="transaction"),
    url(r"^buy/(?P<pk>\d+)/$", BuyProduct.as_view(), name="buy"),
    url(r"^signup/$", RegistrationView.as_view(), name="register"),
    url(r"^add_balance/$", AddBalance.as_view(), name="add_balance")
]

