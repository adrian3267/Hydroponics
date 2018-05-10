from django.conf.urls import url, include
from . import views
from django.views.generic import DetailView
from main.models import PageContent


urlpatterns = [
    url(r'^$', views.index, name = 'main'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=PageContent)),
]
