from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^track/$', views.track, name='track'),
    url(r'^post_tracking', views.post_tracking,  name='post_tracking'),
    url(r'^$', views.index, name='index'),
    
]
