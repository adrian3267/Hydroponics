from django.conf.urls import url, include
from django.views.generic import DetailView, ListView
from certification.models import Certification, RequiredCertificationDocuments
from . import views

urlpatterns = [
    url(r'^new$', views.index, name = 'certification'),
    url(r'^new/(?P<pk>\d+)/$', views.documentsView, name ='certification_second_step'),
    url(r'^overview/$', views.overview, name = 'overview'),
    url(r'^$', ListView.as_view(queryset=Certification.objects.all().order_by("-id")[:25], template_name="certification/certification-list.html"), name='certification-list'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Certification, template_name='certification/certification.html')),
    url(r'^(?P<pk>\d+)/edit$', views.editCertification, name='certification-edit'),
    url(r'^(?P<pk>\d+)/delete$', views.deleteCertification, name='certification-delete'),
    url(r'^(?P<pk>\d+)/edit2$', views.editDocumentsView, name='certification-edit2'),
]
