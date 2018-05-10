from django.conf.urls import url, include
from django.views.generic import DetailView, ListView
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.overview, name = 'overview'),

]
