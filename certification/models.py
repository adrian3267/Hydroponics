from django.db import models
from authentication.models import SupplierProfile, EmbracoProfile

class Certification(models.Model):
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.CASCADE)
    responsible = models.ForeignKey(EmbracoProfile, on_delete=models.CASCADE)
    code = models.CharField(max_length=140, default='0000')
    product_description = models.CharField(max_length=140, default='')
    revision_ECM = models.IntegerField(default=0)
    revision_last = models.DateField(default=0)
    planned_steps = models.CharField(max_length=140, default='')
    date = models.DateField(default=0)
    submission_reason = models.CharField(max_length=140, default='')
    submission_reason_other = models.CharField(max_length=140, default='', blank=True)
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