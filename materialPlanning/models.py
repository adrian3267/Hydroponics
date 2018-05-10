from django.db import models
from certification.models import RequiredCertificationDocuments
from authentication.models import EmbracoProfile

class MaterialPlanning(models.Model):
    document = models.OneToOneField(RequiredCertificationDocuments, on_delete=models.PROTECT)
    development_responsible_name = models.CharField(max_length=50, default='')
    development_responsible_phone = models.CharField(max_length=20, default='+00 00 0000 0000')
    development_responsible_email = models.EmailField()
    material_planning_responsible_name = models.CharField(max_length=50, default='')
    material_planning_responsible_phone = models.CharField(max_length=20, default='+00 00 0000 0000')
    material_planning_responsible_email = models.EmailField()
    commercial_responsible_name = models.CharField(max_length=50, default='')
    commercial_responsible_phone = models.CharField(max_length=20, default='+00 00 0000 0000')
    commercial_responsible_email = models.EmailField()
    observations = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.document

class CommercialInformationEmbraco(models.Model):
    material_planning = models.ForeignKey(MaterialPlanning,on_delete=models.PROTECT)
    minimum_batch_delivery = models.IntegerField(default=0)
    multiple_batch = models.IntegerField(default=0)
    stock_level_at_supplier = models.IntegerField(default=0)
    frequency_of_delivery = models.CharField(max_length=50, default='')
    lead_time = models.IntegerField(default=0)

    def __str__(self):
        return self.material_planning

class CommercialInformationSupplier(models.Model):
    material_planning = models.ForeignKey(MaterialPlanning,on_delete=models.PROTECT)
    minimum_batch_delivery = models.IntegerField(default=0)
    multiple_batch = models.IntegerField(default=0)
    stock_level_at_supplier = models.IntegerField(default=0)
    frequency_of_delivery = models.CharField(max_length=50, default='')
    lead_time = models.IntegerField(default=0)

    def __str__(self):
        return self.material_planning


class MaterialApproval(models.Model):
    commercial_information_supplier = models.OneToOneField(CommercialInformationSupplier, on_delete=models.PROTECT)
    responsible = models.ForeignKey(EmbracoProfile, on_delete=models.PROTECT)
    approved = models.BooleanField(default=False)
    date = models.DateField(default=0)

    def __str__(self):
        return approved



