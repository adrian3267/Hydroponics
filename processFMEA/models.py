from django.db import models
from certification.models import RequiredCertificationDocuments

class ProcessFMEA(models.Model):
    document = models.OneToOneField(RequiredCertificationDocuments, on_delete=models.PROTECT)
    participants = models.CharField(max_length=100,default='')
    coordinators = models.CharField(max_length=50,default='')
    coordinator_area = models.CharField(max_length=50,default='')
    issue_date = models.DateField()
    review_number = models.IntegerField(default=0)
    review_date = models.DateField()
    remarks = models.IntegerField(default=0)

    def __str__(self):
        return self.document

class DetectionProcess(models.Model):
    oportunity_to_detection = models.CharField(max_length=50,default='')
    detection_probability_by_process_controls = models.CharField(max_length=50,default='')
    typical_control_means = models.CharField(max_length=50,default='')
    classification = models.IntegerField(default=0)
    detection_probability = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.classification

class OccurrenceProcess(models.Model):
    failure_probability = models.CharField(max_length=50,default='')
    occurrence_of_cause = models.CharField(max_length=50,default='')
    classification = models.IntegerField(default=0)

    def __str__(self):
        return self.classification

class SeverityProcess(models.Model):
    effect = models.CharField(max_length=50,default='')
    severity_on_product_effect = models.CharField(max_length=50,default='')
    classification = models.IntegerField(default=0)
    product_effect = models.CharField(max_length=50,default='')
    severity_on_product_process = models.CharField(max_length=50,default='')

    def __str(self):
        return self.classification

class FMEA(models.Model):
    process_fmea = models.ForeignKey(ProcessFMEA, on_delete=models.PROTECT)
    item_or_function = models.CharField(max_length=50,default='')
    potencial_failure_mode = models.CharField(max_length=50,default='')
    potencial_failure_effects = models.CharField(max_length=50,default='')
    severity = models.IntegerField(default=0)
    potencial_cause = models.CharField(max_length=50,default='')
    occurrence = models.IntegerField(default=0)
    current_process_control = models.CharField(max_length=50,default='')
    detection = models.IntegerField(default=0)
    risk_number = models.IntegerField(default=0)
    recommended_actions = models.CharField(max_length=150,default='')
    actions_taken = models.CharField(max_length=150,default='')
    implementation_date = models.DateField()
    severity_result = models.IntegerField(default=0)
    occurrence_result = models.IntegerField(default=0)
    detection_result = models.IntegerField(default=0)
    risk_number_result = models.IntegerField(default=0)

    def __str__(self):
        return self.item_or_function