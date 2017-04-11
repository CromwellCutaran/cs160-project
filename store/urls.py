from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^track', views.track, name='track'),
    url(r'^post', views.post,  name='post'),
    url(r'^$', views.index, name='index'),
    
]
