from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^track/$', views.track, name='track'),
    url(r'^post_tracking', views.post_tracking,  name='post_tracking'),
    url(r'^$', views.index, name='index'),
    url(r'^products', views.products, name='products'),
    url(r'^cart', views.cart, name='cart'),
    url(r'^update_cart', views.update_cart, name='update_cart'),
    url(r'^decrement_in_cart', views.decrement_in_cart, name='decrement_in_cart'),
    url(r'^increment_in_cart', views.increment_in_cart, name='increment_in_cart'),
    url(r'^tracking', views.tracking, name='tracking')
]