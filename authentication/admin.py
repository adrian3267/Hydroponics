import django.contrib
from authentication.models import EmbracoProfile, SupplierProfile

django.contrib.admin.site.register(EmbracoProfile)
django.contrib.admin.site.register(SupplierProfile)
