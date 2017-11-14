from django.conf.urls import url
from orders.views import *


urlpatterns = [
    url(r'^create/$', order_create, name='order_create'),
]
