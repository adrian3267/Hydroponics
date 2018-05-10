from django.db import models
from certification.models import RequiredCertificationDocuments
from authentication.models import EmbracoProfile

class PackagingRequirements(models.Model):
    packaging_description = models.OneToOneField(RequiredCertificationDocuments,on_delete=models.PROTECT)
    packaging_type = models.CharField(max_length=20, default='Type')
    start_date = models.DateField()
    container_type = models.CharField(max_length=20, default='Container Type')
    weight_per_batch = models.FloatField(default=0)
    weight_per_pallet = models.FloatField(default=0)
    sku_qtd_per_pallet = models.IntegerField(default=0)
    container_length = models.FloatField(default=0)
    container_width = models.FloatField(default=0)
    container_height = models.FloatField(default=0)
    pallet_length = models.FloatField(default=0)
    pallet_width = models.FloatField(default=0)
    pallet_height = models.FloatField(default=0)
    container_per_layer = models.IntegerField(default=0)
    parts_per_container = models.IntegerField(default=0)
    layers_per_pallet = models.IntegerField(default=0)
    containers_per_pallet = models.IntegerField(default=0)
    pieces_per_pallet = models.IntegerField(default=0)

    def __str__(self):
        return self.packagingDescription

class SupplierPackagingDescription(models.Model):
    packaging_description = models.ForeignKey(RequiredCertificationDocuments, on_delete=models.PROTECT)
    packaging_type = models.CharField(max_length=20, default='Type')
    start_date = models.DateField()
    container_type = models.CharField(max_length=20, default='Container Type')
    weight_per_batch = models.FloatField(default=0)
    weight_per_pallet = models.FloatField(default=0)
    sku_qtd_per_pallet = models.IntegerField(default=0)
    container_length = models.FloatField(default=0)
    container_width = models.FloatField(default=0)
    container_height = models.FloatField(default=0)
    pallet_length = models.FloatField(default=0)
    pallet_width = models.FloatField(default=0)
    pallet_height = models.FloatField(default=0)
    container_per_layer = models.IntegerField(default=0)
    parts_per_container = models.IntegerField(default=0)
    layers_per_pallet = models.IntegerField(default=0)
    containers_per_pallet = models.IntegerField(default=0)
    pieces_per_pallet = models.IntegerField(default=0)
    packaging_image = models.FileField(upload_to='/static/packaging-images/')

class PackagingApproval(models.Model):
    packaging = models.OneToOneField(SupplierPackagingDescription, on_delete=models.PROTECT)
    responsible = models.ForeignKey(EmbracoProfile, on_delete=models.PROTECT)
    approved = models.BooleanField(default=False)
    date = models.DateField(default=0)

    def __str__(self):
        return approved