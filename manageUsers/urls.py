from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.manageUsers, name = 'manage-users'),
    url(r'^(?P<action>\w+)$', views.manageUsers, name = 'manage-users-embraco'),
    url(r'^embraco/new/$', views.createEmbracoUser, name = 'new-user'),
    url(r'^supplier/new/$', views.createSupplierUser, name = 'new-supplier'),
    url(r'^embraco/(?P<pk>\d+)$', views.editEmbracoUser, name = 'edit-user-info'),
    url(r'^supplier/(?P<pk>\d+)$', views.editSupplierUser, name = 'edit-supplier-info'),
]
