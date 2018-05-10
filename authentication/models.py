from django.db import models
from django.contrib.auth.models import User

class EmbracoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=20, default='+00 00 0000 0000')
    department = models.CharField(max_length=50, default='')
    jobTitle = models.CharField(max_length=50, default='')
    is_administrator = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class SupplierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supplierCode = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=15, default='')
    contactPerson = models.CharField(max_length=50,default='')
    phoneNumber = models.CharField(max_length=20, default='+00 00 0000 0000')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name