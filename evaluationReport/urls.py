from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.characteristics, name = 'evaluation_report_main'),
    url(r'^characteristics/$', views.characteristics, name = 'characteristics'),
]
