from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    url(r'^products', views.products, name='products'),
    url(r'^cart', views.cart, name='cart'),
    url(r'^update_cart', views.update_cart, name='update_cart'),
    url(r'^tracking', views.tracking, name='tracking')
]