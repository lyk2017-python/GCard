from django.conf.urls import url
from payment.views import hView, pList, pDetail, card

urlpatterns = [
    url(r"^$",hView.as_view(), name="home"),
    url(r"^product/(?P<slug>[A-Za-z0-9-]+)$",pList.as_view()),
    url(r"^detail/(?P<pk>d+)-(?P<slug>[A-Za-z0-9\-]+)$",pDetail.as_view(), name="product_detail"),
    url(r"^card/(?P<slug>[A-Za-z0-9\-]+)$",card.as_view(), name="card_detail"), ]
