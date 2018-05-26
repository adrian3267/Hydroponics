from django.conf.urls import url, include
from django.views.generic import DetailView, ListView
from myveggarden.models import Garden, GardenSet

from . import views

urlpatterns = [
    url(r'^new$', views.addMeasure, name = 'add_measure'),
    url(r'^change_setpoints$', views.changeSetpoints, name = 'change_setpoints'),
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.overview, name = 'overview'),
    url(r'^history$', ListView.as_view(queryset=Garden.objects.all().order_by("-id")[:25], template_name="myveggarden.measure-list.html"), name='garden_history'),
    url(r'^get/(?P<pk>\d+)/$', views.getSetpoints, name='get-parameters'),
]
