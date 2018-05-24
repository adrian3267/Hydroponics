from django.db import models
from authentication.models import SupplierProfile, EmbracoProfile

class GardenSet(models.Model):
    concentration_set = models.CharField(max_length=140, default='')
    next_cycle_set = models.CharField(max_length=140, default='')

class Garden(models.Model):
    concentration = models.CharField(max_length=140, default='')
    next_cycle = models.CharField(max_length=140, default='')
    

class Certification(models.Model):
    code = models.CharField(max_length=140, default='0000')
    product_description = models.CharField(max_length=140, default='')
    date = models.DateField(default=0)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class Documents(models.Model):
    document_name = models.CharField(max_length=140, default='')

    def __str__(self):
        return self.document_name

class RequiredCertificationDocuments(models.Model):
    certification = models.ForeignKey(Certification, on_delete=models.PROTECT)
    document_type = models.ForeignKey(Documents, on_delete=models.PROTECT)

    def __str__(self):
        return self.document_type

class CertificationApproval(models.Model):
    certification = models.ForeignKey(Certification, on_delete=models.PROTECT)
    responsible = models.ForeignKey(EmbracoProfile, on_delete=models.PROTECT)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.approved

class MeasurementSystem(models.Model):
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.PROTECT)
    name = models.CharField(max_length=140, default='')
    unit = models.CharField(max_length=140, default='')
    measurable = models.BooleanField(default=False)
    resolution = models.FloatField(default=0)
    percentualRnR = models.FloatField(default=0)

    def __str__(self):
        return self.name
